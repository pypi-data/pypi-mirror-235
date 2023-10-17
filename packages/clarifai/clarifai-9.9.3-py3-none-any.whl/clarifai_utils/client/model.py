import os
import time
from typing import Dict, Generator, List

from clarifai_grpc.grpc.api import resources_pb2, service_pb2
from clarifai_grpc.grpc.api.resources_pb2 import Input
from clarifai_grpc.grpc.api.status import status_code_pb2
from google.protobuf.json_format import MessageToDict

from clarifai.client.base import BaseClient
from clarifai.client.lister import Lister
from clarifai.errors import UserError
from clarifai.urls.helper import ClarifaiUrlHelper
from clarifai.utils.logging import get_logger
from clarifai.utils.misc import BackoffIterator


class Model(Lister, BaseClient):
  """Model is a class that provides access to Clarifai API endpoints related to Model information."""

  def __init__(self,
               url_init: str = "",
               model_id: str = "",
               model_version: Dict = {'id': ""},
               output_config: Dict = {'min_value': 0},
               base_url: str = "https://api.clarifai.com",
               **kwargs):
    """Initializes a Model object.

    Args:
        url_init (str): The URL to initialize the model object.
        model_id (str): The Model ID to interact with.
        model_version (dict): The Model Version to interact with.
        output_config (dict): The output config to interact with.
          min_value (float): The minimum value of the prediction confidence to filter.
          max_concepts (int): The maximum number of concepts to return.
          select_concepts (list[Concept]): The concepts to select.
          sample_ms (int): The number of milliseconds to sample.
        base_url (str): Base API url. Default "https://api.clarifai.com"
        **kwargs: Additional keyword arguments to be passed to the Model.
    """
    if url_init != "" and model_id != "":
      raise UserError("You can only specify one of url_init or model_id.")
    if url_init == "" and model_id == "":
      raise UserError("You must specify one of url_init or model_id.")
    if url_init != "":
      user_id, app_id, _, model_id, model_version_id = ClarifaiUrlHelper.split_clarifai_url(
          url_init)
      model_version = {'id': model_version_id}
      kwargs = {'user_id': user_id, 'app_id': app_id}
    self.kwargs = {**kwargs, 'id': model_id, 'model_version': model_version,
                   'output_info': {'output_config': output_config}}
    self.model_info = resources_pb2.Model(**self.kwargs)
    self.logger = get_logger(logger_level="INFO")
    BaseClient.__init__(self, user_id=self.user_id, app_id=self.app_id, base=base_url)
    Lister.__init__(self)

  def create_model_version(self, **kwargs) -> 'Model':
    """Creates a model version for the Model.

    Args:
        **kwargs: Additional keyword arguments to be passed to Model Version.
          - description (str): The description of the model version.
          - concepts (list[Concept]): The concepts to associate with the model version.
          - output_info (resources_pb2.OutputInfo(): The output info to associate with the model version.

    Returns:
        Model: A Model object for the specified model ID.

    Example:
        >>> from clarifai.client.model import Model
        >>> model = Model("model_url")
                    or
        >>> model = Model(model_id='model_id', user_id='user_id', app_id='app_id')
        >>> model_version = model.create_model_version(description='model_version_description')
    """
    request = service_pb2.PostModelVersionsRequest(
        user_app_id=self.user_app_id,
        model_id=self.id,
        model_versions=[resources_pb2.ModelVersion(**kwargs)])

    response = self._grpc_request(self.STUB.PostModelVersions, request)
    if response.status.code != status_code_pb2.SUCCESS:
      raise Exception(response.status)
    self.logger.info("\nModel Version created\n%s", response.status)

    kwargs.update({'app_id': self.app_id, 'user_id': self.user_id})
    dict_response = MessageToDict(response, preserving_proto_field_name=True)
    kwargs = self.process_response_keys(dict_response['model'], 'model')

    return Model(**kwargs)

  def list_versions(self, page_no: int = None,
                    per_page: int = None) -> Generator['Model', None, None]:
    """Lists all the versions for the model.

    Args:
        page_no (int): The page number to list.
        per_page (int): The number of items per page.

    Yields:
        Model: Model objects for the versions of the model.

    Example:
        >>> from clarifai.client.model import Model
        >>> model = Model("model_url") # Example URL: https://clarifai.com/clarifai/main/models/general-image-recognition
                    or
        >>> model = Model(model_id='model_id', user_id='user_id', app_id='app_id')
        >>> all_model_versions = list(model.list_versions())

    Note:
        Defaults to 16 per page if page_no is specified and per_page is not specified.
        If both page_no and per_page are None, then lists all the resources.
    """
    request_data = dict(
        user_app_id=self.user_app_id,
        model_id=self.id,
    )
    all_model_versions_info = self.list_pages_generator(
        self.STUB.ListModelVersions,
        service_pb2.ListModelVersionsRequest,
        request_data,
        per_page=per_page,
        page_no=page_no)

    for model_version_info in all_model_versions_info:
      model_version_info['id'] = model_version_info['model_version_id']
      del model_version_info['model_version_id']
      yield Model(model_id=self.id, **dict(self.kwargs, model_version=model_version_info))

  def predict(self, inputs: List[Input]):
    """Predicts the model based on the given inputs.

    Args:
        inputs (list[Input]): The inputs to predict, must be less than 128.
    """
    if len(inputs) > 128:
      raise UserError("Too many inputs. Max is 128.")  # TODO Use Chunker for inputs len > 128

    request = service_pb2.PostModelOutputsRequest(
        user_app_id=self.user_app_id,
        model_id=self.id,
        version_id=self.model_version.id,
        inputs=inputs,
        model=self.model_info)

    start_time = time.time()
    backoff_iterator = BackoffIterator()
    while True:
      response = self._grpc_request(self.STUB.PostModelOutputs, request)

      if response.outputs and \
        response.outputs[0].status.code == status_code_pb2.MODEL_DEPLOYING and \
        time.time() - start_time < 60 * 10: # 10 minutes
        self.logger.info(f"{self.id} model is still deploying, please wait...")
        time.sleep(next(backoff_iterator))
        continue

      if response.status.code != status_code_pb2.SUCCESS:
        raise Exception(f"Model Predict failed with response {response.status!r}")
      else:
        break

    return response

  def predict_by_filepath(self, filepath: str, input_type: str):
    """Predicts the model based on the given filepath.

    Args:
        filepath (str): The filepath to predict.
        input_type (str): The type of input. Can be 'image', 'text', 'video' or 'audio.

    Example:
        >>> from clarifai.client.model import Model
        >>> model = Model("model_url") # Example URL: https://clarifai.com/clarifai/main/models/general-image-recognition
                    or
        >>> model = Model(model_id='model_id', user_id='user_id', app_id='app_id')
        >>> model_prediction = model.predict_by_filepath('/path/to/image.jpg', 'image')
        >>> model_prediction = model.predict_by_filepath('/path/to/text.txt', 'text')
    """
    if input_type not in ['image', 'text', 'video', 'audio']:
      raise UserError('Invalid input type it should be image, text, video or audio.')
    if not os.path.isfile(filepath):
      raise UserError('Invalid filepath.')

    with open(filepath, "rb") as f:
      file_bytes = f.read()

    return self.predict_by_bytes(file_bytes, input_type)

  def predict_by_bytes(self, input_bytes: bytes, input_type: str):
    """Predicts the model based on the given bytes.

    Args:
        input_bytes (bytes): File Bytes to predict on.
        input_type (str): The type of input. Can be 'image', 'text', 'video' or 'audio'.

    Example:
        >>> from clarifai.client.model import Model
        >>> model = Model("https://clarifai.com/anthropic/completion/models/claude-v2")
        >>> model_prediction = model.predict_by_bytes(b'Write a tweet on future of AI', 'text')
    """
    if input_type not in {'image', 'text', 'video', 'audio'}:
      raise UserError('Invalid input type it should be image, text, video or audio.')
    if not isinstance(input_bytes, bytes):
      raise UserError('Invalid bytes.')
    # TODO will obtain proto from input class
    if input_type == "image":
      input_proto = resources_pb2.Input(
          data=resources_pb2.Data(image=resources_pb2.Image(base64=input_bytes)))
    elif input_type == "text":
      input_proto = resources_pb2.Input(
          data=resources_pb2.Data(text=resources_pb2.Text(raw=input_bytes)))
    elif input_type == "video":
      input_proto = resources_pb2.Input(
          data=resources_pb2.Data(video=resources_pb2.Video(base64=input_bytes)))
    elif input_type == "audio":
      input_proto = resources_pb2.Input(
          data=resources_pb2.Data(audio=resources_pb2.Audio(base64=input_bytes)))

    return self.predict(inputs=[input_proto])

  def predict_by_url(self, url: str, input_type: str):
    """Predicts the model based on the given URL.

    Args:
        url (str): The URL to predict.
        input_type (str): The type of input. Can be 'image', 'text', 'video' or 'audio.

    Example:
        >>> from clarifai.client.model import Model
        >>> model = Model("model_url") # Example URL: https://clarifai.com/clarifai/main/models/general-image-recognition
                    or
        >>> model = Model(model_id='model_id', user_id='user_id', app_id='app_id')
        >>> model_prediction = model.predict_by_url('url', 'image')
    """
    if input_type not in {'image', 'text', 'video', 'audio'}:
      raise UserError('Invalid input type it should be image, text, video or audio.')
    # TODO will be obtain proto from input class
    if input_type == "image":
      input_proto = resources_pb2.Input(
          data=resources_pb2.Data(image=resources_pb2.Image(url=url)))
    elif input_type == "text":
      input_proto = resources_pb2.Input(data=resources_pb2.Data(text=resources_pb2.Text(url=url)))
    elif input_type == "video":
      input_proto = resources_pb2.Input(
          data=resources_pb2.Data(video=resources_pb2.Video(url=url)))
    elif input_type == "audio":
      input_proto = resources_pb2.Input(
          data=resources_pb2.Data(audio=resources_pb2.Audio(url=url)))

    return self.predict(inputs=[input_proto])

  def __getattr__(self, name):
    return getattr(self.model_info, name)

  def __str__(self):
    init_params = [param for param in self.kwargs.keys()]
    attribute_strings = [
        f"{param}={getattr(self.model_info, param)}" for param in init_params
        if hasattr(self.model_info, param)
    ]
    return f"Model Details: \n{', '.join(attribute_strings)}\n"

import datetime
import inspect
from typing import Any

def get_api_key():
    pass

def promptlayer_api_handler():
    pass

def promptlayer_api_handler_async():
    pass


class PromptLayerBase(object):
    __slots__ = ["_obj", "__weakref__", "_function_name", "_provider_type"]

    def __init__(self, obj, function_name="", provider_type="openai"):
        object.__setattr__(self, "_obj", obj)
        object.__setattr__(self, "_function_name", function_name)
        object.__setattr__(self, "_provider_type", provider_type)

    # __getattr__은 클래스에 정의되지 않은 속성에 접근을 시도했을 때
    def __getattr__(self, name):
        # 즉, PromptLayerBase에는 없지만 이 클래스의 _obj의 속성이 name으로 들어왔을 때
        attr = getattr(object.__getattribute__(self, "_obj"), name)
        # 이 속성이 뭔지 모르기 때문에 체크
        if inspect.isclass(attr) or inspect.isfunction(attr) or inspect.ismethod(attr):
            return PromptLayerBase(
                attr,
                function_name=f'{object.__getattribute__(self, "_function_name")}.{name}',
                provider_type=object.__getattribute__(self, "_provider_type")
            )
        return attr

    def __delattr__(self, name):
        delattr(object.__getattribute__(self, "_obj"), name)

    def __setattr__(self, name, value):
        """
        import promptlayer

        openai = promptlayer.openai
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        """
        # 자기 자신의 속성이 아니라 자신이 가진 obj의 속성에 값을 넣어주기 위해서 이렇게 씀
        setattr(object.__getattribute__(self, "_obj"), name, value)

    def __call__(self, *args, **kwargs):
        tags = kwargs.pop("pl_tags", None)
        if tags is not None and not isinstance(tags, list):
            raise Exception("pl_tags must be a list of strings.")
        return_pl_id = kwargs.pop("return_pl_id", False)
        request_start_time = datetime.datetime.now().timestamp()
        function_object = object.__getattribute__(self, "_obj")
        if inspect.isclass(function_object):
            return PromptLayerBase(
                function_object(*args, **kwargs),
                function_name=object.__getattribute__(self, "_function_name"),
                provider_type=object.__getattribute__(self, "_provider_type"),
            )
        if inspect.iscoroutinefunction(function_object):

            async def async_wrapper(*args, **kwargs):
                response = await function_object(*args, **kwargs)
                request_end_time = datetime.datetime.now().timestamp()
                return await promptlayer_api_handler_async(
                    object.__getattribute__(self, "_function_name"),
                    object.__getattribute__(self, "_provider_type"),
                    args,
                    kwargs,
                    tags,
                    response,
                    request_start_time,
                    request_end_time,
                    get_api_key(),
                    return_pl_id=return_pl_id,
                )
            return async_wrapper(*args, **kwargs)
        response = function_object(*args, **kwargs)
        request_end_time = datetime.datetime.now().timestamp()
        return promptlayer_api_handler(
            object.__getattribute__(self, "_function_name"),
            object.__getattribute__(self, "_provider_type"),
            args,
            kwargs,
            tags,
            response,
            request_start_time,
            request_end_time,
            get_api_key(),
            return_pl_id=return_pl_id,
        )
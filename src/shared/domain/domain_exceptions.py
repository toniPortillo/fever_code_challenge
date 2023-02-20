class DomainException(Exception):
    def __init__(
        self,
        domain_artifact: str = "",
        standard_exception: str = "",
        exception_message: str = "",
    ) -> None:
        self.__domain_artifact = domain_artifact
        self.__standard_exception = standard_exception
        self.__exception_message = exception_message

    @property
    def domain_artifact(
        self,
    ) -> str:
        return self.__domain_artifact

    @property
    def standard_exception(
        self,
    ) -> str:
        return self.__standard_exception

    @property
    def exception_message(
        self,
    ) -> str:
        return self.__exception_message

from abc import ABC, abstractmethod

class BaseDeviceProtocol(ABC):
    @abstractmethod
    async def read(self) -> str:
        pass

    @abstractmethod
    async def write(self, message: str) -> None:
        pass
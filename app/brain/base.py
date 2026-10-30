from abc import ABC, abstractmethod


class BaseBrain(ABC):
    """Abstract base interface for V.I.D.U.R. AI brain providers."""

    @abstractmethod
    def ask(self, prompt: str) -> str:
        """Send a user prompt to the brain and return the text response."""
        pass

    @abstractmethod
    def reset(self) -> None:
        """Reset conversation history."""
        pass


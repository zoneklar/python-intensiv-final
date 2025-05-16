"""
Facebook Button:

zwei Events: like und dislike
drei Zustände: Empty, liked, disliked

-----------------------
LIKE       DISLIKE

Zustand:

Wenn ich like drücke:
- wenn Zustand Emty => wird der Zustand liked
- wenn Zustand liked ist => wird der Zustand empty
- wenn Zustand diskliked => wird der Zustand liked

Wenn ich dislikie:
- wenn Zustand Emty => wird der Zustand disliked
- wenn Zustand liked ist => wird der Zustand disliked
- wenn Zustannd diskliked => wird der Zustand empty
"""

from enum import Enum, auto


class LikeState(Enum):
    """Der Zustand des Facebook-Widgets."""

    EMPTY = auto()
    LIKED = auto()
    DISLIKED = auto()


def press_like(state: LikeState) -> LikeState | None:
    """Return next state when Liked Button is pressed."""
    return {
        LikeState.EMPTY: LikeState.LIKED,
        LikeState.LIKED: LikeState.EMPTY,
        LikeState.DISLIKED: LikeState.LIKED,
    }.get(state)


def press_dislike(state: LikeState) -> LikeState | None:
    """Return next state when DisLiked Button is pressed."""
    return {
        LikeState.EMPTY: LikeState.DISLIKED,
        LikeState.LIKED: LikeState.DISLIKED,
        LikeState.DISLIKED: LikeState.EMPTY,
    }.get(state)


intitial_state = LikeState.EMPTY
print("Result empty->liked:", press_like(intitial_state))
print("Result liked_empty:", press_like(LikeState.LIKED))
print("Result disliked:", press_like(LikeState.DISLIKED))

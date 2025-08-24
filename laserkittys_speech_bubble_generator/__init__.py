import importlib.util
krita_spec = importlib.util.find_spec("krita")
if krita_spec is not None:
    from .laserkittys_speech_bubble_generator import *
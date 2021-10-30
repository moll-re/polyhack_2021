from models import user, events
from apis import sbb

SBB = sbb.SBBWrapper()

ret = SBB.wrapper.locations.get(params={"name":"Zürich"})
print(ret[:3])

# def load_events()
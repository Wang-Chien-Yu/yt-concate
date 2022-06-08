from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException

inputs = {
    'channel_id':'UCKSVUHI9rbbkXhvAXK-2uxA'
}
steps = [
    GetVideoList(),
]

for step in steps:
    try:
        step.process()
    except StepException as e:
        print('Exception happend', e)
        break





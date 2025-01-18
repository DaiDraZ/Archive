

import time


import random
from sound import SFX




game_dialogue = {
    "Character Exploration": [
        {"character": "Explorer", "dialogue": "The unknown always calls to me."},
        {"character": "Explorer", "dialogue": "Every journey starts with a single step."},
        {"character": "Explorer", "dialogue": "This map hints at something extraordinary."},
        {"character": "Explorer", "dialogue": "I wonder what secrets the ruins hold."},
        {"character": "Explorer", "dialogue": "The stars above guide my path."},
        {"character": "Explorer", "dialogue": "Each artifact tells a story of its own."},
        {"character": "Explorer", "dialogue": "Nature is the greatest mystery of all."},
        {"character": "Explorer", "dialogue": "Sometimes, the journey matters more than the destination."},
        {"character": "Explorer", "dialogue": "I can almost hear the whispers of the past."},
        {"character": "Explorer", "dialogue": "This compass has never failed me."},
        {"character": "Explorer", "dialogue": "Through the forest, over the mountains, I will find it."},
        {"character": "Explorer", "dialogue": "Danger lies ahead, but so does discovery."},
        {"character": "Explorer", "dialogue": "A true explorer fears nothing but ignorance."},
        {"character": "Explorer", "dialogue": "The wind carries tales of forgotten lands."},
        {"character": "Explorer", "dialogue": "In every shadow, there is a clue waiting to be uncovered."},
        {"character": "Explorer", "dialogue": "This place feels alive with history."},
        {"character": "Explorer", "dialogue": "Even the smallest detail can reveal the biggest truth."},
        {"character": "Explorer", "dialogue": "I have to document everything carefully."},
        {"character": "Explorer", "dialogue": "The thrill of discovery drives me forward."},
        {"character": "Explorer", "dialogue": "The ground beneath us is a tapestry of time."},
        {"character": "Explorer", "dialogue": "What lies beyond that horizon?"},
        {"character": "Explorer", "dialogue": "This artifact glows with a strange energy."},
        {"character": "Explorer", "dialogue": "I feel like I’ve been here before."},
        {"character": "Explorer", "dialogue": "The deeper we go, the more fascinating it becomes."},
        {"character": "Explorer", "dialogue": "I’ll need to sketch this for my notes."},
        {"character": "Explorer", "dialogue": "Time has worn this place, but its essence remains."},
        {"character": "Explorer", "dialogue": "Every step brings us closer to the truth."},
        {"character": "Explorer", "dialogue": "The echo of the past lingers here."},
        {"character": "Explorer", "dialogue": "I must be careful; this ground feels unstable."},
        {"character": "Explorer", "dialogue": "The tools of an explorer: curiosity and courage."},
        {"character": "Explorer", "dialogue": "A faint trail, barely visible, but promising."},
        {"character": "Explorer", "dialogue": "I can feel the pulse of something extraordinary."},
        {"character": "Explorer", "dialogue": "The air grows colder; we must be close."},
        {"character": "Explorer", "dialogue": "The writings on this wall are ancient."},
        {"character": "Explorer", "dialogue": "Something tells me this isn’t just any ordinary artifact."},
        {"character": "Explorer", "dialogue": "I’ve never seen plants like these before."},
        {"character": "Explorer", "dialogue": "Each step feels like treading on history itself."},
        {"character": "Explorer", "dialogue": "The light here behaves so strangely."},
        {"character": "Explorer", "dialogue": "Even in silence, this place speaks volumes."},
        {"character": "Explorer", "dialogue": "I’ll need more supplies to go further."},
        {"character": "Explorer", "dialogue": "Every artifact holds a piece of the puzzle."},
        {"character": "Explorer", "dialogue": "How did they build this with such precision?"},
        {"character": "Explorer", "dialogue": "There’s a pattern here, I just need to find it."},
        {"character": "Explorer", "dialogue": "The smell of earth and stone is invigorating."},
        {"character": "Explorer", "dialogue": "The sound of water nearby must mean a stream or river."},
        {"character": "Explorer", "dialogue": "Even the smallest hint can lead to great discoveries."},
        {"character": "Explorer", "dialogue": "The shadows hide more than meets the eye."},
        {"character": "Explorer", "dialogue": "This artifact radiates an unexplainable warmth."},
        {"character": "Explorer", "dialogue": "I need to decipher these symbols."},
        {"character": "Explorer", "dialogue": "Every question answered leads to ten more."},
        {"character": "Explorer", "dialogue": "The journey is long, but the reward is worth it."},
        {"character": "Explorer", "dialogue": "This is unlike anything I’ve ever encountered."},
        {"character": "Explorer", "dialogue": "The wind whispers secrets only the brave can hear."},
        {"character": "Explorer", "dialogue": "I must press on; the answers are close."},
        {"character": "Explorer", "dialogue": "The texture of this stone is remarkable."},
        {"character": "Explorer", "dialogue": "My instincts tell me we’re not alone."},
        {"character": "Explorer", "dialogue": "The deeper I go, the more I’m drawn in."},
        {"character": "Explorer", "dialogue": "These markings look like a map."},
        {"character": "Explorer", "dialogue": "I have to be meticulous; one mistake could ruin everything."},
        {"character": "Explorer", "dialogue": "The beauty of this place is overwhelming."},
        {"character": "Explorer", "dialogue": "It feels like I’m stepping into a different world."},
        {"character": "Explorer", "dialogue": "I have to trust my instincts on this."},
        {"character": "Explorer", "dialogue": "The artifact’s placement seems deliberate."},
        {"character": "Explorer", "dialogue": "This discovery could change everything."},
        {"character": "Explorer", "dialogue": "I can’t let fear hold me back now."},
        {"character": "Explorer", "dialogue": "The lines carved here are so intricate."},
        {"character": "Explorer", "dialogue": "The energy here feels alive."},
        {"character": "Explorer", "dialogue": "My heart races with every step forward."},
        {"character": "Explorer", "dialogue": "The artifact fits perfectly into this slot."},
        {"character": "Explorer", "dialogue": "This place must have been magnificent in its prime."},
        {"character": "Explorer", "dialogue": "What civilization could have created this?"},
        {"character": "Explorer", "dialogue": "The balance of nature and architecture is astounding."},
        {"character": "Explorer", "dialogue": "Each clue builds the story piece by piece."},
        {"character": "Explorer", "dialogue": "I can’t stop now; the truth is within reach."},
        {"character": "Explorer", "dialogue": "The colors here are like nothing I’ve seen before."},
        {"character": "Explorer", "dialogue": "The air is thick with mystery."},
        {"character": "Explorer", "dialogue": "This engraving is more detailed than I imagined."},
        {"character": "Explorer", "dialogue": "I’ll need to make a rubbing of this for study later."},
        {"character": "Explorer", "dialogue": "I feel like the answers are just out of reach."},
        {"character": "Explorer", "dialogue": "This discovery will be remembered for generations."},
        {"character": "Explorer", "dialogue": "The shadows seem to watch my every move."},
        {"character": "Explorer", "dialogue": "This puzzle is more complex than I thought."},
        {"character": "Explorer", "dialogue": "Every creak and groan of this place tells a story."},
        {"character": "Explorer", "dialogue": "The artifact’s glow intensifies as I approach."},
        {"character": "Explorer", "dialogue": "I’ll have to be careful; this could be a trap."},
        {"character": "Explorer", "dialogue": "The silence here is almost deafening."},
        {"character": "Explorer", "dialogue": "I can’t believe my eyes; this is incredible."},
        {"character": "Explorer", "dialogue": "The journey has been worth every hardship."},
        {"character": "Explorer", "dialogue": "This is a discovery of a lifetime."}
    ]
}



class Story():
    def __init__(self, number_story: int) -> None:
        self.n_story: int = number_story
        pass

    def run(self):
        line = game_dialogue["Character Exploration"][self.n_story]
        print(f"{line["character"]} : ", end=" ")
        for story in line["dialogue"]:
            if story == " ":
                time.sleep(1/random.randint(20,50))
            print(story, end="", flush=True)
            SFX().player_typing()
            time.sleep(0.05)
        print(end="\n")
        time.sleep(2)

# Story(1).run()
# Story(2).run()
# Story(3).run()

import sys

# TODO: Import `Markov`
from markovian.models.markov import Markov

def identify_speaker(speech1, speech2, speech3, k):
    """
    Given sample text from two speakers (1 and 2), and text from an
    unidentified speaker (3), return a tuple with the *normalized* log probabilities
    of each of the speakers uttering that text under a "k-order"
    character-based Markov model, and a conclusion of which speaker
    uttered the unidentified text based on the two probabilities.
    """
    modelA = Markov(k, speech1)
    modelB = Markov(k, speech2)

    # normalize the probabilities for display
    probA = modelA.log_probability(speech3) / len(speech3)
    probB = modelB.log_probability(speech3) / len(speech3)

    return probA, probB, "A" if probA > probB else "B"


def run():
    if len(sys.argv) != 5:
        print(
            f"Usage: python3 {sys.argv[0]} <filenameA> <filenameB> <filenameC> <k>"
        )
        sys.exit(1)

    # TODO: extract parameters from sys.argv & convert types as needed
    command_list = [sys.arg[0], sys.arg[1], sys.arg[2], sys.arg[3], sys.arg[4]]

    # TODO: open files & read text
    with open(sys.argv[1], "r") as f:
        speakerA_text = f.read()

    with open(sys.argv[2], "r") as f:
        speakerB_text = f.read()

    with open(sys.argv[3], "r") as f:
        unknown_speaker_text = f.read()
    # TODO: call identify_speaker & print results
    id_speaker = self.identify_speaker(speakerA_text, speakerB_text, unknown_speaker_text)
    probA, probB, speaker = id_speaker
    print("Speaker A: {} Speaker B: {} Conclusion: Speaker {} is most likely".format(probA, probB, speaker))
    # Output should resemble (values will differ based on inputs):

    # Speaker A: -2.1670591295191572
    # Speaker B: -2.2363636778055525
    # Conclusion: Speaker A is most likely

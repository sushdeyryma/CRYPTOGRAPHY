import matplotlib.pylab as plt

# these are the letters we are interested in when dealing with frequency-analysis
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# the method to do frequency analysis: we just count the occurrences of the given characters
def frequency_analysis(text):
    # the text we analysis
    text = text.upper()

    # we use a dictionary to store the letter-frequency pair
    letter_frequency = {}

    # initialize the dictionary (of course with 0 frequencies)
    for letter in LETTERS:
        letter_frequency[letter] = 0

    # let's consider the text we want to analyse
    for letter in text:
        # we keep incrementing the occurrence of the given letter
        if letter in LETTERS:
            letter_frequency[letter] += 1

    return letter_frequency


# plot the histogram of the letter-frequency pairs
def plot_distribution(letter_frequency):
    plt.bar(letter_frequency.keys(), letter_frequency.values())
    plt.show()


def caesar_crack(text):
    freq = frequency_analysis(text)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print("The possible key value: %s" % (LETTERS.find(freq[0][0]) -
                                          LETTERS.find('E')))


if __name__ == '__main__':
    # I have used key=8
    cipher_text = 'UGVIUMQAJITIHAPWTKHMZQIUNZWUJCLIXMABPCVOIZGQIUYCITQNQMLIAIXPGAQKQABIBBPMUWUMVBQIUEWZSQVOIAIAQUCTIBQWVMVOQVMMZIBIUCTBQVIBQWVITKWUXIVGQPIDMJMMVQVBMZMABMLQVITOWZQBPUAIVLLIBIABZCKBCZMAIVLQBAQUXTMUMVBIBQWVAMAXMKQITTGQVRIDIAQVKMCVQDMZAQBGTIBMZWVQOWBIKYCIQVBMLEQBPUIKPQVMTMIZVQVOBMKPVQYCMAIZBQNQKQITQVBMTTQOMVKMVCUMZQKITUMBPWLAIVLZMKQXMAACKPIAAWTDQVOLQNNMZMVBQITMYCIBQWVATQVMIZITOMJZIQVBMZXWTIBQWVIVLMFBZIXWTIBQWVBPMAMBPQVOAUIGXZWDMBWJMDMZGDMZGQUXWZBIVBQVAMDMZITNQMTLAAWNBEIZMMVOQVMMZQVOZMAMIZKPIVLLMDMTWXUMVBWZQVDMABUMVBJIVSQVOQPIDMIAXMKQITILLQKBQWVBWYCIVBQBIBQDMUWLMTAACKPIABPMJTIKSAKPWTMAUWLMTWZBPMUMZBWVUWLMT'
    caesar_crack(cipher_text)

import math
import matplotlib.pyplot as plt

# sineBool = True means sine wave; false means cosine wave
def getSamples(freq, amp, phase, sampRate, numSamples, sineBool):
    samples = []
    for i in range(numSamples):
        if sineBool:
            samples.append(amp * math.sin((2 * math.pi * freq * i * 1/sampRate) + phase))
        else:
            samples.append(amp * math.cos((2 * math.pi * freq * i * 1/sampRate) + phase))
    return samples

def dotProduct(samp1, samp2):
    sampSum = 0
    for i in range(len(samp1)):
        sampSum += samp1[i] * samp2[i]
    return sampSum

if __name__ == "__main__":
    # Orthogonality will only hold if (f_1*N)/f_o is an integer and (f_2*N)/f_o is also
    # an integer.
    # 
    # There is an additional caveat that f_1/f_o - f_2/f_o and f_1/f_o + f_2/f_o cannot be integers.
    # Otherwise you will possibly get a non-zero result.  This should not be an issue if f_1 and f_2
    # are properly less than f_o.

    f_1 = 3
    f_2 = 2
    f_o = 104 # sample rate
    N = 104

    print("Number of complete cycles for frequency 1:", f_1*N/f_o)
    print("Number of complete cycles for frequency 2:", f_2*N/f_o)

    amp1 = 1
    amp2 = 0.5
    phase1 = math.pi/2
    phase2 = 1
    samp1 = getSamples(f_1, amp1, phase1, f_o, N, True)
    samp2 = getSamples(f_2, amp2, phase2, f_o, N, False)
    print("Dot product with", f_1, "and", f_2, ":", dotProduct(samp1, samp2))
    
    plt.style.use('ggplot')
    plt.figure(figsize = (5, 3))
    plt.plot(range(N), samp1, '-b', range(N), samp2, '-g')
    
    # Can comment this out
    numPlotPoints = 8
    xPoints = range(0, len(samp1), N//numPlotPoints)
    yPoints1 = samp1[::N//numPlotPoints]
    yPoints2 = samp2[::N//numPlotPoints]
    print(yPoints1)
    print(yPoints2)
    print("Dot product with", f_1, "and", f_2, "at a sample rate of", numPlotPoints, ":", dotProduct(yPoints1, yPoints2))
    plt.plot(xPoints, yPoints1, 'ob', xPoints, yPoints2, 'og')

    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.xticks([0, N], [0, "L"])
    plt.tight_layout()
    plt.savefig("plot")
    plt.show()

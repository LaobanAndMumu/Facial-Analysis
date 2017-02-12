import cognitive_face as CF
import math


class faceAnalysis:

    slots = 'landmarks','width','height','left','top'

    KEY = '71bd3fbf693a4f68a35bb10a4843a1a2'
    CF.Key.set(KEY)

    def __init__(self, filePath):
        """
        This function initializes the object and creates
        a dictionary of 27 facial landmarks.
        :param filePath: A string representing the file path
                         to an image (JPEG, PNG, GIF ( 1st frame),
                         and BMP).
        """

        image = CF.face.detect( filePath, landmarks=True)[0]
        rectangle = image["faceRectangle"]
        self.width = rectangle["width"]
        self.height = rectangle["height"]
        self.left = rectangle["left"]
        self.top = rectangle["top"]
        self.landmarks = image["faceLandmarks"]


    def eyebrowDist(self):
        outLeft = self.landmarks["eyebrowLeftInner"]["x"]
        outRight = self.landmarks["eyebrowRightInner"]["x"]

        percentage = abs(outLeft - outRight)/self.width

        if percentage >= 0.20:
            return "long_distance"
        return "short_distance"

    def eyebrowLength(self):
        deltaLeft = abs(self.landmarks["eyebrowLeftInner"]["x"] -
                        self.landmarks["eyebrowLeftOuter"]["x"])
        deltaRight = abs(self.landmarks["eyebrowRightInner"]["x"] -
                        self.landmarks["eyebrowRightOuter"]["x"])
        avgLength = (deltaLeft+deltaRight)/2

        if avgLength >= 0.30:
            return "long"
        return "short"

    def eyebrowAngle(self):

        leftX = abs(self.landmarks["eyebrowLeftInner"]["x"] -
                        self.landmarks["eyebrowLeftOuter"]["x"])
        leftY = abs(self.landmarks["eyebrowLeftInner"]["y"] -
                        self.landmarks["eyebrowLeftOuter"]["y"])
        leftAngle = math.atan( leftY / leftX ) * (180/math.pi)

        rightX = abs(self.landmarks["eyebrowRightInner"]["x"] -
                        self.landmarks["eyebrowRightOuter"]["x"])
        rightY = abs(self.landmarks["eyebrowRightInner"]["y"] -
                        self.landmarks["eyebrowRightOuter"]["y"])
        rightAngle = math.atan( rightY / rightX ) * (180/math.pi)

        avgAngle = (leftAngle+rightAngle)/2

        if avgAngle >= 10.0:
            return "angled"
        return "flat"

    def eyeSize(self):

        leftX = abs(self.landmarks["eyeLeftInner"]["x"] -
                        self.landmarks["eyeLeftOuter"]["x"])
        rightX = abs(self.landmarks["eyeRightInner"]["x"] -
                        self.landmarks["eyeRightOuter"]["x"])
        avgX = (leftX + rightX )/2

        leftY = abs(self.landmarks["eyeLeftTop"]["y"] -
                        self.landmarks["eyeLeftBottom"]["y"])
        rightY = abs(self.landmarks["eyeRightTop"]["y"] -
                        self.landmarks["eyeRightBottom"]["y"])
        avgY = (leftY + rightY)/2

        percentX = avgX/self.width
        percentY = avgY/self.height
        ratio = percentX/percentY

        if ratio < 2.0:
            return "round"
        elif ratio >= 2.0 and ratio < 2.3:
            return "short_narrow"
        elif ratio >= 2.3 and ratio < 2.5:
            return "big_wide"
        else:
            return "long_narrow"

    def noseHeight(self):

        avgTop = ( self.landmarks["noseRootLeft"]["y"] + self.landmarks["noseRootRight"]["y"])/2
        avgBottom = ( self.landmarks["noseLeftAlarTop"]["y"] + self.landmarks["noseRightAlarTop"]["y"])/2
        totalHeight = abs(avgBottom - avgTop)
        percent = totalHeight/self.height

        if percent < 0.15:
            return "short"
        return "tall"

    def noseWidth(self):

        nostrilWidth = abs(self.landmarks["noseLeftAlarOutTip"]["x"] - self.landmarks["noseRightAlarOutTip"]["x"])
        percent = nostrilWidth/self.width
        if percent < 26:
            return "narrow"
        return "wide"


    def mouthHeight(self):
        height = abs(self.landmarks["upperLipTop"]["y"] - self.landmarks["underLipBottom"]["y"])
        percent = height/self.height

        if percent > 0.36:
            return "thick"
        return "thin"


    def mouthWidth(self):
        lipWidth = abs(self.landmarks["mouthLeft"]["x"] - self.landmarks["mouthRight"]["x"])
        percent =  lipWidth / self.width

        if percent > 0.135:
            return "wide"
        return "narrow"

def main():

    keanu = 'Keanu_Reeves_1.jpg'
    try:
        kFace = faceAnalysis(keanu)
        kY = kFace.mouthHeight()
        kX = kFace.mouthWidth()
        print(kFace.width)
        print(kY)
        print(kX)
        print( "Keanu - Percent of width: " + str(kX/kFace.width) )
        print( "Keanu - Percent of width: " + str(kY/kFace.height) )

    except:
        print("No internet, try again later")

    morgan = 'Freeman.jpg'
    try:
        mFace = faceAnalysis(morgan)
        mY = mFace.mouthHeight()
        mX = mFace.mouthWidth()
        print(mFace.width)
        print(mY)
        print(mX)
        print( "Morgan - Percent of width: " + str(mX/mFace.width))
        print( "Morgan - Percent of width: " + str(mY/mFace.height))

    except:
        print("No internet, try again later")


    lily = 'lily-collins.jpg'
    try:
        lFace = faceAnalysis(lily)
        lY = lFace.mouthHeight()
        lX = lFace.mouthWidth()
        print(lFace.width)
        print(lY)
        print(lX)
        print( "Lily - Percent of width: " + str(lX/lFace.width))
        print( "Lily - Percent of width: " + str(lY/lFace.height))

    except:
        print("No internet, try again later")

    jennifer = 'Jennifer.jpg'
    try:
        jFace = faceAnalysis(jennifer)
        jY = jFace.mouthHeight()
        jX = jFace.mouthWidth()
        print(jFace.width)
        print(jY)
        print(jX)
        print( "Jennifer - Percent of width: " + str(jX/jFace.width))
        print( "Jennifer - Percent of width: " + str(jY/jFace.height))

    except:
        print("No internet, try again later")

    kelly = 'kelly.png'
    try:
        keFace = faceAnalysis(kelly)
        keY = keFace.mouthHeight()
        keX = keFace.mouthWidth()
        print(keFace.width)
        print(keY)
        print(keX)
        print( "Kelly - Percent of width: " +str(keX/keFace.width))
        print( "Kelly - Percent of width: " +str(keY/keFace.height))

    except:
        print("No internet, try again later")

    harriet = 'Harriet.jpg'
    try:
        hFace = faceAnalysis(harriet)
        hY = hFace.mouthHeight()
        hX = hFace.mouthWidth()
        print(hFace.width)
        print(hY)
        print(hX)
        print( "Harriet - Percent of width: " + str(hX/hFace.width))
        print( "Harriet - Percent of width: " + str(hY/hFace.height))

    except:
        print("No internet, try again later")

    rachel = 'Rachel.jpg'
    try:
        rFace = faceAnalysis(rachel)
        rY = rFace.mouthHeight()
        rX = rFace.mouthWidth()
        print(rFace.width)
        print(rY)
        print(rX)
        print("Rachel - Percent of width: " + str(rX / rFace.width))
        print("Rachel - Percent of width: " + str(rY / rFace.height))

    except:
        print("No internet, try again later")

    Angelina = 'Angelina.jpg'
    try:
        aFace = faceAnalysis(Angelina)
        aY = aFace.mouthHeight()
        aX = aFace.mouthWidth()
        print(aFace.width)
        print(aY)
        print(aX)
        print("Angelina - Percent of width: " + str(aX / aFace.width))
        print("Angelina - Percent of width: " + str(aY / aFace.height))

    except:
        print("No internet, try again later")



if __name__ == '__main__':
    main()






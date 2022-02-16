import unittest
from translate import translate

class TestTranslate(unittest.TestCase):
    """
    Tests the translator against multiple words.

    Should translate, phrases, paragraphs, or books.
    """

    def test_translate_phrases(self):
        phrases = [
            'Can you help me?',
            'When is lunch?',
            'Did you study?',
            'Am I winning?',
            'What\'s for dinner?',
            'Call me later.',
            'Please send money.',
            'Let\'s go to the store.',
            'Playing baseball is fun.',
            'Moonlight is lovely.',
            'I need a new toothbrush.'
        ]
        translations = [
            'Ancay ouyay elphay emay?',
            'Enwhay isyay unchlay?',
            'Idday ouyay udystay?',
            'Amyay Iyay inningway?',
            'Atswhay orfay innerday?',
            'Allcay emay aterlay.',
            'Easeplay endsay oneymay.',
            'Etslay ogay otay ethay orestay.',
            'Ayingplay aseballbay isyay unfay.',
            'Oonlightmay isyay ovelylay.',
            'Iyay eednay ayay ewnay oothbrushtay.'
        ]

        for index, phrase in enumerate(phrases):
            translation = translate(phrase)
            self.assertEqual(translation, translations[index])

    def test_translate_psalm47(self):
        psalm_47 = """
            Oh, clap your hands, all you peoples!
            Shout to God with the voice of triumph!
            For the LORD Most High is awesome;
            He is a great King over all the earth.
            He will subdue the peoples under us,
            And the nations under our feet.
            He will choose our inheritance for us,
            The excellence of Jacob whom He loves.

            God has gone up with a shout,
            The LORD with the sound of a trumpet.
            Sing praises to God, sing praises!
            Sing praises to our King, sing praises!
            For God is the King of all the earth;
            Sing praises with understanding.

            God reigns over the nations;
            God sits on His holy throne.
            The princes of the people have gathered together,
            The people of the God of Abraham.
            For the shields of the earth belong to God;
            He is greatly exalted.
        """

        translated_psalm = """
            Ohyay, apclay ouryay andshay, allyay ouyay eoplespay!
            Outshay otay Odgay ithway ethay oicevay ofyay iumphtray!
            Orfay ethay ORDLAY Ostmay Ighhay isyay awesomeyay;
            Ehay isyay ayay eatgray Ingkay overyay allyay ethay earthyay.
            Ehay illway ubduesay ethay eoplespay underyay usyay,
            Andyay ethay ationsnay underyay ouryay eetfay.
            Ehay illway oosechay ouryay inheritanceyay orfay usyay,
            Ethay excellenceyay ofyay Acobjay omwhay Ehay oveslay.

            Odgay ashay onegay upyay ithway ayay outshay,
            Ethay ORDLAY ithway ethay oundsay ofyay ayay umpettray.
            Ingsay aisespray otay Odgay, ingsay aisespray!
            Ingsay aisespray otay ouryay Ingkay, ingsay aisespray!
            Orfay Odgay isyay ethay Ingkay ofyay allyay ethay earthyay;
            Ingsay aisespray ithway understandingyay.

            Odgay eignsray overyay ethay ationsnay;
            Odgay itssay onyay Ishay olyhay ronethay.
            Ethay incespray ofyay ethay eoplepay avehay atheredgay ogethertay,
            Ethay eoplepay ofyay ethay Odgay ofyay Abrahamyay.
            Orfay ethay ieldsshay ofyay ethay earthyay elongbay otay Odgay;
            Ehay isyay eatlygray exaltedyay.
        """

        translation = translate(psalm_47)
        self.assertEqual(translation, translated_psalm)



    def test_translate_poem(self):
        # Resignation - Henry Wadsworth Longfellow
        resignation_poem = """
            There is no flock, however watched and tended,
            But one dead lamb is there!
            There is no fireside, howsoe'er defended,
            But has one vacant chair!

            The air is full of farewells to the dying,
            And mournings for the dead;
            The heart of Rachel, for her children crying,
            Will not be comforted!

            Let us be patient!  These severe afflictions
            Not from the ground arise,
            But oftentimes celestial benedictions
            Assume this dark disguise.

            We see but dimly through the mists and vapors;
            Amid these earthly damps
            What seem to us but sad, funereal tapers
            May be heaven's distant lamps.

            There is no Death!  What seems so is transition;
            This life of mortal breath
            Is but a suburb of the life elysian,
            Whose portal we call Death.

            She is not dead -- the child of our affection --
            But gone unto that school
            Where she no longer needs our poor protection,
            And Christ himself doth rule.

            In that great cloister's stillness and seclusion,
            By guardian angels led,
            Safe from temptation, safe from sin's pollution,
            She lives, whom we call dead.

            Day after day we think what she is doing
            In those bright realms of air;
            Year after year, her tender steps pursuing,
            Behold her grown more fair.

            Thus do we walk with her, and keep unbroken
            The bond which nature gives,
            Thinking that our remembrance, though unspoken,
            May reach her where she lives.

            Not as a child shall we again behold her;
            For when with raptures wild
            In our embraces we again enfold her,
            She will not be a child;

            But a fair maiden, in her Father's mansion,
            Clothed with celestial grace;
            And beautiful with all the soul's expansion
            Shall we behold her face.

            And though at times impetuous with emotion
            And anguish long suppressed,
            The swelling heart heaves moaning like the ocean,
            That cannot be at rest,--

            We will be patient, and assuage the feeling
            We may not wholly stay;
            By silence sanctifying, not concealing,
            The grief that must have way.
        """

        translated_poem = """
            Erethay isyay onay ockflay, oweverhay atchedway andyay endedtay,
            Utbay oneyay eadday amblay isyay erethay!
            Erethay isyay onay iresidefay, owsoeerhay efendedday,
            Utbay ashay oneyay acantvay airchay!

            Ethay airyay isyay ullfay ofyay arewellsfay otay ethay yingday,
            Andyay ourningsmay orfay ethay eadday;
            Ethay earthay ofyay Achelray, orfay erhay ildrenchay yingcray,
            Illway otnay ebay omfortedcay!

            Etlay usyay ebay atientpay!  Esethay everesay afflictionsyay
            Otnay omfray ethay oundgray ariseyay,
            Utbay oftentimesyay elestialcay enedictionsbay
            Assumeyay isthay arkday isguiseday.

            Eway eesay utbay imlyday roughthay ethay istsmay andyay aporsvay;
            Amidyay esethay earthlyyay ampsday
            Atwhay eemsay otay usyay utbay adsay, unerealfay aperstay
            Aymay ebay eavenshay istantday ampslay.

            Erethay isyay onay Eathday!  Atwhay eemssay osay isyay ansitiontray;
            Isthay ifelay ofyay ortalmay eathbray
            Isyay utbay ayay uburbsay ofyay ethay ifelay elysianyay,
            Osewhay ortalpay eway allcay Eathday.

            Eshay isyay otnay eadday -- ethay ildchay ofyay ouryay affectionyay --
            Utbay onegay untoyay atthay hoolscay
            Erewhay eshay onay ongerlay eedsnay ouryay oorpay otectionpray,
            Andyay Ristchay imselfhay othday uleray.

            Inyay atthay eatgray oistersclay illnessstay andyay eclusionsay,
            Ybay uardiangay angelsyay edlay,
            Afesay omfray emptationtay, afesay omfray inssay ollutionpay,
            Eshay iveslay, omwhay eway allcay eadday.

            Ayday afteryay ayday eway inkthay atwhay eshay isyay oingday
            Inyay osethay ightbray ealmsray ofyay airyay;
            Earyay afteryay earyay, erhay endertay epsstay ursuingpay,
            Eholdbay erhay owngray oremay airfay.

            Usthay oday eway alkway ithway erhay, andyay eepkay unbrokenyay
            Ethay ondbay ichwhay aturenay ivesgay,
            Inkingthay atthay ouryay emembranceray, oughthay unspokenyay,
            Aymay eachray erhay erewhay eshay iveslay.

            Otnay asyay ayay ildchay allshay eway againyay eholdbay erhay;
            Orfay enwhay ithway apturesray ildway
            Inyay ouryay embracesyay eway againyay enfoldyay erhay,
            Eshay illway otnay ebay ayay ildchay;

            Utbay ayay airfay aidenmay, inyay erhay Athersfay ansionmay,
            Othedclay ithway elestialcay acegray;
            Andyay eautifulbay ithway allyay ethay oulssay expansionyay
            Allshay eway eholdbay erhay acefay.

            Andyay oughthay atyay imestay impetuousyay ithway emotionyay
            Andyay anguishyay onglay uppressedsay,
            Ethay ellingsway earthay eaveshay oaningmay ikelay ethay oceanyay,
            Atthay annotcay ebay atyay estray,--

            Eway illway ebay atientpay, andyay assuageyay ethay eelingfay
            Eway aymay otnay ollywhay aystay;
            Ybay ilencesay anctifyingsay, otnay oncealingcay,
            Ethay iefgray atthay ustmay avehay ayway.
        """

        translation = translate(resignation_poem)
        self.assertEqual(translation, translated_poem)


if __name__ == '__main__':
    unittest.main()

import time
import random

phrases = ["Greater love has no one than this: to lay down one's life for one's friends.",
           "Now to him who is able to do immeasurably more than all we ask or imagine, according to his power that is at work within us.",
           "Be strong and courageous. Do not be afraid or terrified because of them, or the LORD your God goes with you; he will never leave you nor forsake you.",
           "The LORD is my light and my salvation; whom shall I fear? The LORD is the stronghold of my life; of whom shall I be afraid?",
           "There is no fear in love. But perfect love drives out fear, because fear has to do with punishment. The one who fears is not made perfect in love.",
           "What, then, shall we say in response to these things? If God is for us, who can be against us?",
           "May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit.",
           "Be strong, and let your heart take courage, all you who wait for the LORD!",
           "Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you, I will uphold you with my righteous right hand.",
           "Jesus looked at them and said, ‘With man it is impossible, but not with God. For all things are possible with God.'",
           "Casting all your anxieties on him, because he cares for you.",
           "I can do all things through him who strengthens me.",
           "Therefore, my beloved brothers, be steadfast, immovable, always abounding in the work of the LORD, knowing that in the LORD your labor is not in vain.",
           "Be watchful, stand firm in the faith, act like men, be strong. Let all that you do be done in love.",
           "Give thanks to the LORD for He is good: His love endures forever.",
           "Taste and see that the LORD is good; blessed is the one who takes refuge in him.",
           "And we know that in all things God works for the good of those who love him, who have been called according to his purpose.",
           ]

phrase = phrases[random.randint(0, len(phrases))]

print("Type the given phrase as fast as you can:")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print()
print(phrase)
print()
print("Your turn:")
start = time.time()

text = input()

end = time.time()

corrects = 0

for i in range(len(text)):
        if len(phrase) > i and len(text) > i:
            if phrase[i] == text[i]:
                corrects += 1

words = text.split()

print()
print("Your accuracy is " + str(round((corrects / len(phrase)) * 100, 2)) + "%")
print("Your typing speed is " + str(round((len(text) / (end - start)) * 60)) + " characters per minute")
print("Also known as " + str(round(len(words) / (end - start) * 60)) + " Words per minute")
#create a function that calculates West-Haven score for liver disease
def calculate_west_haven_score(jaundice, ascites, encephalopathy):
    score = 0
    if jaundice:
        score += 1
    if ascites:
        score += 2
    if encephalopathy:
        score += 4
    return score

jaundice = False # boolean for jaundice
ascites = True # boolean for ascites
encephalopathy = True # boolean for encephalopathy

west_haven_score = calculate_west_haven_score(jaundice, ascites, encephalopathy)
print("West-Haven score:", west_haven_score)
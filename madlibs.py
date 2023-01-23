# string concatination 

# another playing :/
def madlib():
    time_of_day = input("Time of Day: ")
    body_part_plural = input("Body Part (plural): ")
    color = input("Color: ")
    verb_past_tense = input("Verb (past tense): ")
    food = input("Food: ")
    noun1 = input("Noun: ")
    noun_plural_1 = input("Noun (plural): ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")


    madlib = f"It was a {adj1} summer {time_of_day} when we realized that the vaccine to stop \
spread of the disease did not work. Instead, it produced ZOMBIES!!! They were thirsty for {body_part_plural} \
and the streets were lined with these monsters holding {noun_plural_1} in their hands. \
Their eyes were {color} with hunger as they {verb_past_tense} around the city looking for {food}. \
They were {adj2} and {adj3}, unknowing how to act in this human world... except eat {body_part_plural}!!!! \
That was their sole mission and they were dedicated towards achieving it for the sake of {noun1}."
    
    print(madlib)

if __name__ == '__main__':
    madlib()

#playing around with concatination methodes <
    color =""
#the first methode 
print ('what is the color of a banana ?\n')
color =input ()
print (f"\n the color of a banana is {color}")
#the second methode
print ('what is the color of an aple ?\n')
color =input ()
print ("\n the color of an aple is {}".format(color))
#the third methode 
print ('what is the color of an orange ?\n')
color =input ()
print ("\n the color of an orange is "+ color )
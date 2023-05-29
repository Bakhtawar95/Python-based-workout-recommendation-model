import random
import pandas as pd

# Read exercise data from Excel file
exercise_data = pd.read_excel('Book1.xlsx')

# Create dictionaries and lists to store exercises for each level
exercise_lists = {}
completed_exercises1_3 = []
completed_exercises3_4 = []
completed_exercises4_5 = []
recommended_exercises1_3b = []
recommended_exercises3_4b=[]
recommended_exercises4_5b=[]
recommended_exercises1_3i = []
recommended_exercises3_4i=[]
recommended_exercises4_5i=[]
recommended_exercises1_3a = []
recommended_exercises3_4a=[]
recommended_exercises4_5a=[]

# Loop through the exercise data and append exercises to the appropriate exercise list
for index, row in exercise_data.iterrows():
    level = row['Level']
    exercise = row['Exercise']
    if level not in exercise_lists:
        exercise_lists[level] = []
    exercise_lists[level].append(exercise)

# Shuffle the exercise lists for each level
#for level in exercise_lists:
    #random.shuffle(exercise_lists[level])

# Create separate lists for each level
level_1_exercises = exercise_lists.get(1, [])
level_2_exercises = exercise_lists.get(2, [])
level_3_exercises = exercise_lists.get(3, [])
level_4_exercises = exercise_lists.get(4, [])
level_5_exercises = exercise_lists.get(5, [])

level1_3_exercises = level_1_exercises + level_3_exercises
level3_4_exercises = level_3_exercises + level_4_exercises
level4_5_exercises = level_4_exercises + level_5_exercises


# Loops to recommend exercises
for i in range(1,76):
    if (i % 5 == 0 and i !=1) :
        recommended_exercises1_3b.append(random.choice(level_2_exercises))
    else:
       recommended_exercises1_3b.append(random.choice(level1_3_exercises))

for i in range(1,151):
    if (i % 5 == 0 and i !=1) :
        recommended_exercises3_4b.append(random.choice(level_2_exercises))
    else:
        recommended_exercises3_4b.append(random.choice(level3_4_exercises))

for i in range(1,226):
    if (i % 5 == 0 and i !=1) :
        recommended_exercises4_5b.append(random.choice(level_2_exercises))
    else:
        recommended_exercises4_5b.append(random.choice(level4_5_exercises))

#loops for Intermediate type
for i in range(1,121):
    if (i % 5 == 0 and i !=1) :
        recommended_exercises1_3i.append(random.choice(level_2_exercises))
    else:
       recommended_exercises1_3i.append(random.choice(level1_3_exercises))

for i in range(1,241):
    if (i % 5 == 0 and i !=1) :
        recommended_exercises3_4i.append(random.choice(level_2_exercises))
    else:
        recommended_exercises3_4i.append(random.choice(level3_4_exercises))

for i in range(1,361):
    if (i % 5 == 0 and i !=1) :
        recommended_exercises4_5i.append(random.choice(level_2_exercises))
    else:
        recommended_exercises4_5i.append(random.choice(level4_5_exercises))
#loops for Intermediate type
for i in range(1,151):
    if (i % 5 == 0 and i !=1) :
        recommended_exercises1_3a.append(random.choice(level_2_exercises))
    else:
       recommended_exercises1_3a.append(random.choice(level1_3_exercises))
for i in range(1,301):
    if (i % 5 == 0 and i !=1) :
        recommended_exercises3_4a.append(random.choice(level_2_exercises))
    else:
        recommended_exercises3_4a.append(random.choice(level3_4_exercises))

for i in range(1,451):
    if (i % 5 == 0 and i !=1) :
        recommended_exercises4_5a.append(random.choice(level_2_exercises))
    else:
        recommended_exercises4_5a.append(random.choice(level4_5_exercises))


def questionaire(exercise,list_name,completed_exercise_group):
    answer = input("Could you do the exercise? (Provide yes or no) ")
    if answer == "yes" or answer == "Yes" or answer == "yeah" or answer == "Yeah":
        print("That's great")
        completed_exercise_group.append(exercise)  # Append exercise to completed exercises list
    elif answer == "no" or answer == "No" or answer == "Nope" or answer == "nope":
        print("No Problem.Please answer carefully:")
        ans2=input("Why weren't you able to do the exercise? e.g. it's painful/it's too heavy: ")
        second_popup(list_name,completed_exercise_group)



def second_popup(list_name,completed_exercise_group):
    if len(completed_exercise_group)!=0:
        latest_exercise = completed_exercise_group[-1]
        for key, value in exercise_lists.items():
            if latest_exercise in value:
                level=key
               # print(f"Latest element corresponds to key: {level}")
          # Exit the loop after finding the corresponding key
            # Select an exercise from value list that is not in completed_exercises1_3 list
             
                selected_exercise = None
                for exercise in value:
                    if exercise not in completed_exercise_group:
                        selected_exercise = exercise
                        print(f"If you weren't able to do the previous exercise. Here's another recommendation for you: {selected_exercise }")
                        questionaire(selected_exercise,list_name,completed_exercise_group)
                        break
                    #break  # Exit the loop after finding the selected exercise
                    else:
                        if level in exercise_lists:
                            exercise_list = exercise_lists[level]
                    # Select a random exercise from the same level
                            random_exercise = random.choice(exercise_list)
                            print(f"You can repeat this exercise: {random_exercise}")
                            questionaire(random_exercise,list_name,completed_exercise_group)
                            break  # Exit the loop if no available exercises are found

    else:
    
        string = list_name
        prefix = "completed_exercises"
        level = string[len(prefix)]  # level is the digit immediately following the prefix
        print(f"string:{string}")
        print(f"level:{level}")        
        if int(level) in exercise_lists:
           exercise_list = exercise_lists[int(level)]
           #Select a random exercise from the same level
           random_exercise = random.choice(exercise_list)
           print(f"You can try this one: {random_exercise}")
           questionaire(random_exercise,list_name,completed_exercise_group)


def recommender(criterion,programs,list_name,recommended_exercise_group,completed_exercise_group):
    count=0
    for i, exercise in enumerate(recommended_exercise_group, 1):
    
        if i % criterion ==1 and count<programs:
            print(f"--Program {((i)//criterion+1)}/{programs}")
            print("--------------------------------------------------------------------------")
            count+=1
        if exercise not in completed_exercise_group:
            print(f"Exercise {i}: {exercise}")
            print("--------------------------------------------------------------------------")
            variable = exercise
            search_column = 'Exercise'
            fetch_column = 'Description'
            
# Use boolean indexing to filter rows where the search column matches the variable
            filtered_df = exercise_data[exercise_data[search_column] == variable] 
            
# Fetch the corresponding value from the fetch column
            if not filtered_df['Desc'].isnull().any():
               fetched_value = filtered_df.iloc[0,1]
               print(f"How to do: {fetched_value}")
               print("--------------------------------------------------------------------------")
    # Prompt a question after each exerciseknn
            questionaire(exercise,list_name,completed_exercise_group)
    
            

def main():

    first_list="completed_exercises1_3"
    second_list="completed_exercises3_4"
    third_list="completed_exercises4_5"

    print("-------------------------Workout Recommendations--------------------------")
    print("--------------------------------------------------------------------------")
    level=input("Please select a level of training from below that's most suited for you:\n 1) Beginner\n 2) Intermediate\n 3) Advanced\n")
    print("")

    if level=="Beginner":
        recommender(5,15,first_list,recommended_exercises1_3b,completed_exercises1_3)
        print("You have successfully completed the First level.Now your'e on Second Level:")
        print("--------------------------------------------------------------------------")
        recommender(5,30,second_list,recommended_exercises3_4b,completed_exercises3_4)
        print("The Second Level is completed here.Now you are on Third Level:")
        print("--------------------------------------------------------------------------")
        recommender(5,45,third_list,recommended_exercises4_5b,completed_exercises4_5)
        print("The third Level is also completed.Now your training is finished!")
        print("--------------------------------------------------------------------------")

        

    elif level=="Intermediate":
        recommender(8,15,first_list,recommended_exercises1_3i,completed_exercises1_3)
        print("You have successfully completed the First level.Now your'e on Second Level:")
        print("--------------------------------------------------------------------------")
        recommender(8,30,second_list,recommended_exercises3_4i,completed_exercises3_4)
        print("The Second Level is completed here.Now you are on Third Level:")
        print("--------------------------------------------------------------------------")
        recommender(8,45,third_list,recommended_exercises4_5i,completed_exercises4_5)
        print("The third Level is also completed.Now your training is finished!")
        print("--------------------------------------------------------------------------")

    
    elif level=="Advanced":
        recommender(10,15,first_list,recommended_exercises1_3a,completed_exercises1_3)
        print("You have successfully completed the First level.Now your'e on Second Level:")
        print("--------------------------------------------------------------------------")
        recommender(10,30,second_list,recommended_exercises3_4a,completed_exercises3_4)
        print("The Second Level is completed here.Now you are on Third Level:")
        print("--------------------------------------------------------------------------")
        recommender(10,45,third_list,recommended_exercises4_5a,completed_exercises4_5)
        print("The third Level is also completed.Now your training is finished!")
        print("--------------------------------------------------------------------------")

    else:
        print("Please choose a correct type with spellings exactly as given in the options")
    

    #i=1
    #while i<5:
        #recommender(third_list,recommended_exercises4_5b,completed_exercises4_5.copy())
        #completed_exercises4_5.clear() #Empty the completed exercises list to start recommending the same exercises again   
        #i=i+1


if __name__ == '__main__':
    main()

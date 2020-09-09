#World Series Winners
#Objective: find winning teams for years
def main():
   
   
   year_dict = {} # dict variables
   count_dict = {}
  
   BASE_YEAR = 1903;
  
   
   file_read = open('WorldSeries.txt','r')  # opening file
  
   for line in file_read:  # read the file
       teamName = line.strip()

       year_dict[BASE_YEAR] = teamName # + each team to dict & baseyear & team

       BASE_YEAR += 1; # increase baseyear
      
       cnt = winners(teamName, count_dict) # count winners
      
       if cnt==1: # count and find winning team
           count_dict[teamName] += 1
       else:
           count_dict[teamName] = 1
      
   file_read.close() # close the file
  
   printSorted(count_dict) # show count and year of team
   showResults(year_dict, count_dict)
   

def printSorted(count_dict):
   """ Prints sorted dict """
   from operator import itemgetter
   for k, v in sorted(count_dict.items(), key=itemgetter(1), reverse=True): # Iterating over dictionary
       print(k + " : " + str(v) + " Times")
      
  
def showResults(year_dict, count_dict):

   yeslist=["yes", "y", "yeah","Yes","YES"] 

   year = int(input('\n\nInput a year between 1903-2020: ')) 
   
   if year == 1904 or year == 1994: # results printed
       print("World series was skipped that year", year)
   elif year < 1903 or year > 2020:
       print('Invalid input, input a year betwen 1903-2020 for ex. 1999')
   else:
       winner = year_dict[year]
       wins = count_dict[winner]
       print('The team that won the world series in ', \
       year, ' are the ', winner, '.', sep='')
       print('That team won the series', wins, 'times.')
      
   restart=input("Do you want to play again? Yes or No:").lower()
   if restart in yeslist:
      main()
   else:
      exit()

def winners(team, count_dict):
   if team in count_dict.keys():
       return 1
   else:
       return 0
        
main()

from itertools import islice

basepath="/home/amarnath/openbook1-Am482487/"



def unique_words(book):
    list_uniq=[]
    with open(book, "r") as myfile:
        for line in myfile:
            for word in line.split():
                list_uniq.append(word)
    
    return list(set(list_uniq))
    


def count_the_article(x):

        return len(unique_words(x))


def sorted_words(lst):
    lst.sort(key=len,reverse=True)
    return lst

blist=["Book1.txt","Book2.txt","Book3.txt"]



def character_word_count(book):
    newlist=[]
    with open(book, "r") as myfile:
        for line in myfile:
            for word in line.split():
                newlist.append(word)
    ds = {item: len(item) for item in newlist}  # I  am using dict comprehension 
    
    return ds

def starts_with_vow(book):
    list_vow=[]
    with open(book, "r") as myfile:
        for line in myfile:
            for word in line.split():
                list_vow.append(word)
    counter=0
    vow = "aeiou"

    for i in list_vow:

        for ele in vow:

            if i.startswith(ele):
                counter+=1

    return counter
def rare_words(b):
    #to be done
def unused_words(b):
    #to be done


for i in blist:
    
    unique_words(basepath+i)
    count_the_article(basepath+i)
    sorted_words(unique_words(basepath+i))
    character_word_count(basepath+i)
    print(starts_with_vow(basepath+i))

rare_words(basepath+"20k.txt",basepath+"Book1.txt")





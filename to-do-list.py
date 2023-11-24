book=[]
def insert_tasks():
    book.append(input('input Task: '))

def delete_tasks():
    try:
        deleted_ele=book.pop(int(input('Enter the position: ')))
        print(f'element {deleted_ele} has been deleted')
    except IndexError:
        print('there is no Item to Delete')
def display_tasks():
    print(book)        
i=0
print('---------------------To-Do-List------------------------')
while True:
    print('Operations:')
    
    ch=int(input('\n1.Insert\n2.Delete\n3.Display\n4.Exit\n>>'))
    if ch==1:
        insert_tasks()
    elif ch==2:
        delete_tasks()
    elif ch==3:
        display_tasks()
    elif ch==4:
        break
    elif ch>4:
        print(f'{ch} is a Wrong Choice\n choose 1,2,3 or 4')
        

        
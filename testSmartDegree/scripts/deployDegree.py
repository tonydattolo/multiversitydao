from brownie import (
    accounts,
    config,
    SmartDegree,
    network
)
from scripts.utils import get_account
from dotenv import load_dotenv
load_dotenv()

def deployRinkeby():
    studentAccount = get_account('rinkebyTest1Student')
    instructorAccount = get_account('rinkebyTest4Instructor')
    smartDegree = SmartDegree.deploy({'from': studentAccount}) # accessing SimpleStorage.sol
    # Transact
    # Call
    currentCoursesCompleted = smartDegree.getCoursesCompleted()
    print(f'{currentCoursesCompleted=}')
    
    
    storeCompletedCourse = smartDegree.addCourseCompleted(
        instructorAccount,
        "CS 101",
        "Computer Science 1", 
        {'from': instructorAccount},
        )
    storeCompletedCourse.wait(1)
    
    currentCoursesCompleted = smartDegree.getCoursesCompleted()
    
    print(f'{currentCoursesCompleted=}')

def main():
    deployRinkeby()
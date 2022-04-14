from brownie import (
    accounts,
    config,
    SmartDegree,
    # network
)
from dotenv import load_dotenv
load_dotenv()

def deployAndTestLocal():
    studentAccount = accounts[0]
    instructorAccount = accounts[1]
    smartDegree = SmartDegree.deploy({'from': studentAccount}) # accessing SimpleStorage.sol
    # Transact
    # Call
    currentCoursesCompleted = smartDegree.getCoursesCompleted()
    print(f'{currentCoursesCompleted=}')
    
    
    storeCompletedCourse = smartDegree.addCourseCompleted(
        instructorAccount,
        "CS 101",
        "Intro to CS Example", 
        {'from': studentAccount},
        )
    storeCompletedCourse.wait(1)
    
    currentCoursesCompleted = smartDegree.getCoursesCompleted()
    
    print(f'{currentCoursesCompleted=}')


def deploySmartDegree():
    studentAccount = accounts[0]
    smartDegree = SmartDegree.deploy({'from': studentAccount}) # accessing SimpleStorage.sol
    # Transact
    # Call
    currentCoursesCompleted = smartDegree.getCoursesCompleted()
    print(f'{currentCoursesCompleted=}')
    
    
    storeValueTx = simpleStorage.store(666, {'from': account})
    storeValueTx.wait(1)
    
    currentStoredValue = simpleStorage.retrieve()
    
    print(f'{currentStoredValue=}')

def updateSmartDegree():
    instructorAccount = accounts[1]
    simpleStorage = SimpleStorage.deploy({'from': account}) # accessing SimpleStorage.sol
    # Transact
    # Call
    currentStoredValue = simpleStorage.retrieve()
    print(f'{currentStoredValue=}')
    
    storeValueTx = simpleStorage.store(666, {'from': account})
    storeValueTx.wait(1)
    
    currentStoredValue = simpleStorage.retrieve()
    
    print(f'{currentStoredValue=}')

def main():
    deployAndTestLocal()
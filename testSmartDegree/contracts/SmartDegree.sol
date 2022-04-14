// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SmartDegree {

    // static constant address of student
    address student;

    // course struct
    struct Course {
        address instructor;
        string courseCode;
        string courseName;
    }

    Course[] public coursesTaken;
    mapping (address => Course) public coursesTakenMap;

    // public function that gets an array of courses taken by a student
    function getCoursesCompleted() external view returns (Course[] memory) {
        return coursesTaken;
    }

    // function that adds a course to the coursesTaken array
    function addCourseCompleted(address instructor, string memory courseCode, string memory courseName) public {
        Course memory course = Course(instructor, courseCode, courseName);
        coursesTaken.push(course);
        coursesTakenMap[student] = course;
    }


}

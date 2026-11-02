// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {
    struct Student {
        uint256 id;
        string name;
        uint8 age;
        string course;
    }

    Student[] private students;

    event StudentAdded(uint256 id, string name, string course);
    event FallbackCalled(address sender, uint value, string message);

    function addStudent(uint256 _id, string memory _name, uint8 _age, string memory _course) public {
        students.push(Student(_id, _name, _age, _course));
        emit StudentAdded(_id, _name, _course);
    }

    function getStudent(uint256 index) public view returns (uint256, string memory, uint8, string memory) {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.id, s.name, s.age, s.course);
    }

    function getTotalStudents() public view returns (uint256) {
        return students.length;
    }

    fallback() external payable {
        emit FallbackCalled(msg.sender, msg.value, "Fallback function triggered!");
    }

    receive() external payable {
        emit FallbackCalled(msg.sender, msg.value, "Receive function triggered!");
    }
}

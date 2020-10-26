import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-course',
  templateUrl: './course.component.html',
  styleUrls: ['./course.component.css']
})
export class CourseComponent{

  constructor() { }
  titles = " List of Courses";
  coursess = ["course1","course2","course3"]

}

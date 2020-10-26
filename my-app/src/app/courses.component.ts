import { CoursesService } from './courses.service';
import { from } from 'rxjs';
import {Component} from '@angular/core';


@Component({
    selector: 'courses',
    template: `<h2>{{title }}</h2>
    <ul>
    <li *ngFor = "let course of courses">
        {{course}}
    </li>
 </ul>
    `
})

export class CoursesComponent {
    title = "3 Authors";
    courses;

    constructor(service : CoursesService){
        
        //let service = new CoursesService();
        this.courses = service.getCourses();
    }

    // Logic for calling an HTTP service
}
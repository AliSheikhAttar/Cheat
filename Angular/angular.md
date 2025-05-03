## Structure
| **Type**             | **Purpose**                                                                                           | **Example**                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Component Template   | Contains the HTML that gets displayed to a user                                                       | `app.component.html`                                                        |
| Component Class      | Contains code to run when important events occur (like when a user clicks a button)                   | `app.component.ts`                                                          |
| Property Binding     | Sets a property on an HTML element. Everything in the double quotes is code! Can access any property/method from our component class instance | `<button [disabled]="length">Submit</button>`              |
| Event Binding        | Sets up an event handler on an HTML element. Everything in the double quotes is code! Can call any method on the component class instance    | `<button (click)="onButtonClick()">Submit</button>`         |
| Interpolation        | Prints out information in a template. Can access any property/method from our component class instance | `<div>Your password length is {{ length }}</div>`            |
| Structural Directive | Changes the structure of HTML in a template.                                                          | `<div *ngIf="shouldShowSubmit()">Submit</button></div>`       |

## Flow
![alt text](flow.png)

## Event binding syntax
![alt text](event-binding-syntax.png)
![alt text](event-binding-syntax-1.png)

## Property binding syntax
![alt text](property-binding-syntax.png)
![alt text](property-binding-syntax-1.png)

## interpolation
![alt text](interpolation.png)

## directives
![alt text](directives.png)
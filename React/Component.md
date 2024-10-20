# Component
function-based components 

## Naming convention
pascal : MyExample
## Create component
```bash
touch src/<component>.tsx
```

## components
```bash
mkdir source/components
```

## fragments
```ts
import { Fragment } from "react";
return (
<Fragment>
<elemnet1>
<element2>
</Fragment>
)

# OR

return (
<>
<elemnet1>
<element2>
</>
)
```


## rendering dynamic list
```ts
const items = [list...]

return (
<>
<item>
<ul classname="list-group">
{items.map((item)=>(<li className="list-group-item" key={item}>{item}</li>))}
</ul>
</>
)
```


## conditional rendering
```ts
return (
<>
    <item>
    { items.length == 0 ? <p>msg</p> : null }   
    <ul classname="list-group">
        {items.map((item)=>(<li key={item}>{item}</li>))}
    </ul>
</>
)

# OR

const message = items.length == 0 ? <p>msg</p> : null
return (
<>
    <item>
    {message}   
    <ul classname="list-group">
        {items.map((item)=>(<li key={item}>{item}</li>))}
    </ul>
</>
)

# OR inside var

const message = items.length == 0 ? <p>msg</p> : null
return (
<>
    <item>
    {message}   
    <ul classname="list-group">
        {items.map((item)=>(<li key={item}>{item}</li>))}
    </ul>
</>
)

# OR inside function

const getMessage = () => {
    return items.length == 0 ? <p>msg</p> : null
}
return (
<>
    <item>
    {getMessage()}   
    <ul classname="list-group">
        {items.map((item)=>(<li key={item}>{item}</li>))}
    </ul>
</>
)

# OR shorter way

return (
<>
    <item>
    {items.length == 0 && <p>msg</p>}   
    <ul classname="list-group">
        {items.map((item)=>(<li key={item}>{item}</li>))}
    </ul>
</>
)

```


## Event handling
```ts
import  { MouseEvent } from "react";

function ListGroup(){

const handleClick = (event: MouseEvent) => console.log(event)
return (
<>
    <item>
    {items.length == 0 && <p>msg</p>}   
    <ul classname="list-group">
        {items.map((item)=>(<li key={item} onClick={handleClick}>{item}</li>))}
    </ul>
</>
)
}
```



## Managing states
each component has it own state which we have to declare to react
that this component has variable which might change its state so it will notified
 
```ts
function ListGroup(){

const [selectedIndex, setSelectedIndex] = useState(-1);
return (
<>
    <item>
    {items.length == 0 && <p>msg</p>}   
    <ul classname="list-group" >
        {items.map((item)=>(<li className={selectedIndex === index ? "list-group-item active" : "list-group-item"}
        key={item} 
        onClick={()=> { setSelectedIndex(index); }}>{item}</li>))}
    </ul>
</>
)
}
```

## pass data vio props
```ts
function Component1(){

let mylist = [list...]
return (
<div>
    <Component2 prop1={mylist}, prop2="random" />
</div>
);
}

## Component2
interface Props{
    items:string[];
    heading:string;
}
function Component2(props:Props){
...
{heading}
{props.items}
...

}


## OR
 

interface Props{
    items:string[];
    heading:string;
}
function Component2({ items, heading }:Props){
...
{heading}
{items}
...

}
```
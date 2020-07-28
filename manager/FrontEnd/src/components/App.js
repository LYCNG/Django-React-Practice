import React, { Component} from './node_modules/react';
import ReactDOM from './node_modules/react-dom';

class App extends Component{
    render(){
        return <h1>React App</h1>
    }
}

ReactDOM.render(<App />, document.getElementById('app'));


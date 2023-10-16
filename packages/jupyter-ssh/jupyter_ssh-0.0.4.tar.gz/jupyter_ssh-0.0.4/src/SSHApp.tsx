/// <reference types="webpack-env" />

import { createRoot } from 'react-dom/client';
import SSHJupyterLabHeadless from './SSHJupyterLabHeadless';

const div = document.createElement('div');
document.body.appendChild(div);
const root = createRoot(div)

if (module.hot) {
  module.hot.accept('./SSHJupyterLabHeadless', () => {
    const SSHJupyterLabHeadless = require('./SSHJupyterLabHeadless').default;
    root.render(<SSHJupyterLabHeadless/>);
  })
}

root.render(<SSHJupyterLabHeadless />);

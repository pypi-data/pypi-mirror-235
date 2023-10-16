/// <reference types="webpack-env" />

import { createRoot } from 'react-dom/client';
import DevcontainersJupyterLabHeadless from './DevcontainersJupyterLabHeadless';

const div = document.createElement('div');
document.body.appendChild(div);
const root = createRoot(div)

if (module.hot) {
  module.hot.accept('./DevcontainersJupyterLabHeadless', () => {
    const DevcontainersJupyterLabHeadless = require('./DevcontainersJupyterLabHeadless').default;
    root.render(<DevcontainersJupyterLabHeadless/>);
  })
}

root.render(<DevcontainersJupyterLabHeadless />);

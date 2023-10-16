import { JupyterFrontEnd, JupyterLab } from '@jupyterlab/application';
import { ReactWidget } from '@jupyterlab/apputils';
import { JupyterLabAppAdapter } from '@datalayer/jupyter-react';
import Devcontainers from '../Devcontainers';

export class JupyterDevcontainersWidget extends ReactWidget {
  private _app: JupyterFrontEnd;
  constructor(app: JupyterFrontEnd) {
    super();
    this._app = app;
    this.addClass('dla-Container');
  }

  render(): JSX.Element {
    return <>
      <Devcontainers adapter={JupyterLabAppAdapter.create(this._app as JupyterLab)} />
    </>
  }
}

import { JupyterFrontEnd, JupyterLab } from '@jupyterlab/application';
import { ReactWidget } from '@jupyterlab/apputils';
import { JupyterLabAppAdapter } from '@datalayer/jupyter-react';
import { IJupyterSSH } from './index';
import SSH from '../SSH';

export class JupyterSSHWidget extends ReactWidget {
  private _app: JupyterFrontEnd;
  private _jupyterSSH: IJupyterSSH;
  constructor(app: JupyterFrontEnd, jupyterSSH: IJupyterSSH) {
    super();
    this._app = app;
    this._jupyterSSH = jupyterSSH;
    this.addClass('dla-Container');
  }

  render(): JSX.Element {
    return (
      <>
        <this._jupyterSSH.TimerView />
        <this._jupyterSSH.MobxTimerView mobxTimer={this._jupyterSSH.mobxTimer} />
        <SSH adapter={JupyterLabAppAdapter.create(this._app as JupyterLab)} />
      </>
    )
  }
}

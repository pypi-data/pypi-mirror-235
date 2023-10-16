import { Token } from '@lumino/coreutils';
import { JupyterFrontEnd, JupyterFrontEndPlugin, ILayoutRestorer } from '@jupyterlab/application';
import { MainAreaWidget, ICommandPalette, WidgetTracker } from '@jupyterlab/apputils';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { ILauncher } from '@jupyterlab/launcher';
import icon from '@datalayer/icons-react/data1/LaptopSimpleIconLabIcon';
import { requestAPI } from './handler';
import { JupyterSSHWidget } from './widget';
import { Timer } from "../state";
import { TimerView } from "../timer/TimerView";
import { mobxTimer, MobxTimer, MobxTimerView, IMobxTimerViewProps } from "../state/mobx";

import '../../style/index.css';

export type IJupyterSSH = {
  timer: Timer,
  TimerView: () => JSX.Element,
  mobxTimer: MobxTimer,
  MobxTimerView: (props: IMobxTimerViewProps) => JSX.Element,
};

export const IJupyterSSH = new Token<IJupyterSSH>(
  '@datalayer/jupyter-ssh:plugin'
);

/**
 * The command IDs used by the plugin.
 */
namespace CommandIDs {
  export const create = 'create-jupyter-ssh-widget';
}

/**
 * Initialization data for the @datalayer/jupyter-ssh extension.
 */
const plugin: JupyterFrontEndPlugin<IJupyterSSH> = {
  id: '@datalayer/jupyter-ssh:plugin',
  autoStart: true,
  requires: [ICommandPalette],
  optional: [ISettingRegistry, ILauncher, ILayoutRestorer],
  provides: IJupyterSSH,
  activate: (
    app: JupyterFrontEnd,
    palette: ICommandPalette,
    settingRegistry?: ISettingRegistry,
    launcher?: ILauncher,
    restorer?: ILayoutRestorer,
  ): IJupyterSSH => {
    const { commands } = app;
    const command = CommandIDs.create;
    const tracker = new WidgetTracker<MainAreaWidget<JupyterSSHWidget>>({
      namespace: 'jupyter-ssh',
    });
    if (restorer) {
      void restorer.restore(tracker, {
        command,
        name: () => 'jupyter-ssh',
      });
    }
    const jupyterSSH: IJupyterSSH  = {
      timer: new Timer(),
      TimerView,
      mobxTimer,
      MobxTimerView,
    }
    commands.addCommand(command, {
      caption: 'Show SSH',
      label: 'SSH',
      icon,
      execute: () => {
        const content = new JupyterSSHWidget(app, jupyterSSH);
        const widget = new MainAreaWidget<JupyterSSHWidget>({ content });
        widget.title.label = 'SSH';
        widget.title.icon = icon;
        app.shell.add(widget, 'main');
        tracker.add(widget);
      }
    });
    const category = 'Datalayer';
    palette.addItem({ command, category });
    if (launcher) {
      launcher.add({
        command,
        category,
        rank: 2.4,
      });
    }
    if (settingRegistry) {
      settingRegistry
        .load(plugin.id)
        .then(settings => {
          console.log('@datalayer/jupyter-ssh settings loaded:', settings.composite);
        })
        .catch(reason => {
          console.error('Failed to load settings for @datalayer/jupyter-ssh.', reason);
        });
    }
    requestAPI<any>('config')
      .then(data => {
        console.log(data);
      })
      .catch(reason => {
        console.error(
          `Error while accessing the jupyter server jupyter_ssh extension.\n${reason}`
        );
      }
    );
    console.log('JupyterLab plugin @datalayer/jupyter-ssh is activated!');
    return jupyterSSH;
  }
};

export default plugin;

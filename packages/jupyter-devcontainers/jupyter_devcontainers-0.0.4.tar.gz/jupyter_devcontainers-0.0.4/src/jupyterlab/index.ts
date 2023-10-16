import { Token } from '@lumino/coreutils';
import { JupyterFrontEnd, JupyterFrontEndPlugin, ILayoutRestorer } from '@jupyterlab/application';
import { MainAreaWidget, ICommandPalette, WidgetTracker } from '@jupyterlab/apputils';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { ILauncher } from '@jupyterlab/launcher';
import icon from '@datalayer/icons-react/data2/CodeEditorIconLabIcon';
import { requestAPI } from './handler';
import { JupyterDevcontainersWidget } from './widget';
import { timer, Timer, TimerView, ITimerViewProps } from "../state/mobx";

import '../../style/index.css';

export type IJupyterDevcontainers = {
  timer: Timer,
  TimerView: (props: ITimerViewProps) => JSX.Element,
};

export const IJupyterDevcontainers = new Token<IJupyterDevcontainers>(
  '@datalayer/jupyter-devcontainers:plugin'
);

/**
 * The command IDs used by the plugin.
 */
namespace CommandIDs {
  export const create = 'create-jupyter-devcontainers-widget';
}

/**
 * Initialization data for the @datalayer/jupyter-devcontainers extension.
 */
const plugin: JupyterFrontEndPlugin<IJupyterDevcontainers> = {
  id: '@datalayer/jupyter-devcontainers:plugin',
  autoStart: true,
  requires: [ICommandPalette],
  optional: [ISettingRegistry, ILauncher, ILayoutRestorer],
  provides: IJupyterDevcontainers,
  activate: (
    app: JupyterFrontEnd,
    palette: ICommandPalette,
    settingRegistry?: ISettingRegistry,
    launcher?: ILauncher,
    restorer?: ILayoutRestorer,
  ): IJupyterDevcontainers => {
    const jupyterDevcontainers: IJupyterDevcontainers  = {
      timer,
      TimerView,
    }
    const { commands } = app;
    const command = CommandIDs.create;
    const tracker = new WidgetTracker<MainAreaWidget<JupyterDevcontainersWidget>>({
      namespace: 'jupyter-devcontainers',
    });
    if (restorer) {
      void restorer.restore(tracker, {
        command,
        name: () => 'jupyter-devcontainers',
      });
    }
    commands.addCommand(command, {
      caption: 'Show Devcontainers',
      label: 'Devcontainers',
      icon,
      execute: () => {
        const content = new JupyterDevcontainersWidget(app);
        const widget = new MainAreaWidget<JupyterDevcontainersWidget>({ content });
        widget.title.label = 'Devcontainers';
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
        rank: 2.2,
      });
    }
    if (settingRegistry) {
      settingRegistry
        .load(plugin.id)
        .then(settings => {
          console.log('@datalayer/jupyter-devcontainers settings loaded:', settings.composite);
        })
        .catch(reason => {
          console.error('Failed to load settings for @datalayer/jupyter-devcontainers.', reason);
        });
    }
    requestAPI<any>('config')
      .then(data => {
        console.log(data);
      })
      .catch(reason => {
        console.error(
          `Error while accessing the jupyter server jupyter_devcontainers extension.\n${reason}`
        );
      }
    );
    console.log('JupyterLab plugin @datalayer/jupyter-devcontainers is activated!');
    return jupyterDevcontainers;
  }
};

export default plugin;

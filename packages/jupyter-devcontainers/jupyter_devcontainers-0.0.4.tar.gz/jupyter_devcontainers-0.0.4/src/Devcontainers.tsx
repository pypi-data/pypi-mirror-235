import { useState, useEffect } from 'react';
import { ThemeProvider, BaseStyles, Box } from '@primer/react';
import { UnderlineNav } from '@primer/react/drafts';
import { JupyterLabAppAdapter } from '@datalayer/jupyter-react';
import { CodeEditorIcon } from '@datalayer/icons-react';
import { requestAPI } from './jupyterlab/handler';
import useStore from './state';
import ImagesTab from './tabs/ImagesTab';
import ContainersTab from './tabs/ContainersTab';
import AboutTab from './tabs/AboutTab';

export type DevcontainersProps = {
  adapter?: JupyterLabAppAdapter;
}

const JupyterDevcontainers = (props: DevcontainersProps) => {
  const { setTab, getIntTab } = useStore();
  const intTab = getIntTab();
  const [version, setVersion] = useState('');
  useEffect(() => {
    requestAPI<any>('config')
    .then(data => {
      setVersion(data.version);
    })
    .catch(reason => {
      console.error(
        `Error while accessing the jupyter server jupyter_devcontainers extension.\n${reason}`
      );
    });
  }, []);
  return (
    <>
      <ThemeProvider>
        <BaseStyles>
          <Box>
            <Box>
              <UnderlineNav aria-label="devcontainers">
                <UnderlineNav.Item aria-label="images" aria-current={intTab === 0 ? "page" : undefined} onSelect={e => {e.preventDefault(); setTab(0.0);}}>
                  Images
                </UnderlineNav.Item>
                <UnderlineNav.Item aria-label="containers" aria-current={intTab === 1 ? "page" : undefined}onSelect={e => {e.preventDefault(); setTab(1.0);}}>
                  Containers
                </UnderlineNav.Item>
                <UnderlineNav.Item aria-label="about" aria-current={intTab === 2 ? "page" : undefined} icon={() => <CodeEditorIcon colored/>} onSelect={e => {e.preventDefault(); setTab(2.0);}}>
                  About
                </UnderlineNav.Item>
              </UnderlineNav>
            </Box>
            <Box m={3}>
              {intTab === 0 && <ImagesTab/>}
              {intTab === 1 && <ContainersTab/>}
              {intTab === 2 && <AboutTab version={version} />}
            </Box>
          </Box>
        </BaseStyles>
      </ThemeProvider>
    </>
  );
}

export default JupyterDevcontainers;

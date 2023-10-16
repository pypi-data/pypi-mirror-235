import { useState, useEffect } from 'react';
import { Box, Text } from '@primer/react';
import { Table, DataTable } from '@primer/react/drafts';
import { requestAPI } from '../jupyterlab/handler';
import { strip } from './../utils/Utils';

type DevcontainersImage = {
  id: number,
  RepoTags: string[],
  Os: string,
  Size: number,
  Created: string,
}

const Images = () => {
  const [images, setImages] = useState(new Array<DevcontainersImage>());
  useEffect(() => {
    requestAPI<any>('images')
    .then(data => {
      const images = (data.images as [any]).map((image, id) => {
        return {
          id,
          ...image,
        }
      }) as [DevcontainersImage];
      setImages(images.filter(image => image.RepoTags.length > 0));
    })
    .catch(reason => {
      console.error(
        `Error while accessing the jupyter server jupyter_devcontainers extension.\n${reason}`
      );
    });
  }, []);
  return (
    <>
      <Box>
        <Table.Container>
          <Table.Title as="h2" id="images">
            Devcontainers images
          </Table.Title>
          <Table.Subtitle as="p" id="images-subtitle">
            List of Devcontainers images.
          </Table.Subtitle>
          <DataTable
            aria-labelledby="images"
            aria-describedby="images-subtitle" 
            data={images}
            columns={[
              {
                header: 'RepoTags',
                field: 'RepoTags',
                renderCell: row => <>
                  { row.RepoTags.map(repoTag => <Box><Text>{strip(repoTag, 40)}</Text></Box>) 
                }</>
              },
              {
                header: 'Size',
                field: 'Size',
                renderCell: row => <Text>{row.Size}</Text>
              },
              {
                header: 'Os',
                field: 'Os',
                renderCell: row => <Text>{row.Os}</Text>
              },
            ]}
          />
        </Table.Container>
      </Box>
    </>
  )
}

export default Images;

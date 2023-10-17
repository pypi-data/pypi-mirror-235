import React, { useCallback, useMemo, useState } from 'react';
import { CogniteClient } from '@cognite/sdk/dist/src';
import { Menu } from '@cognite/cogs.js';
import { ReactWidget } from '@jupyterlab/apputils';
import { Cell } from '@jupyterlab/cells';
import { Copilot } from 'cdf-copilot-core';
import { CodeGeneratorInputPanel } from './components/CodeGeneratorInputPanel';

/**
 * A Lumino ReactWidget that wraps a CopilotMenu.
 */
export const CopilotWidget: React.FC<any> = ({
  activeCell,
  sdk
}: {
  activeCell: Cell;
  sdk: CogniteClient;
}): any => {
  return ReactWidget.create(
    <div id="copilot_widget_root">
      <Copilot showChatButton={false} sdk={sdk as any}>
        <CopilotMenu activeCell={activeCell} sdk={sdk} />
      </Copilot>
    </div>
  );
};

const CopilotMenu: React.FC<any> = ({
  activeCell,
  sdk
}: {
  activeCell: Cell;
  sdk: CogniteClient;
}): JSX.Element => {
  const [showRootMenu, setShowRootMenu] = useState(true);
  const [showCodeGenerator, setShowCodeGenerator] = useState(false);

  const onGenerateCodeClick = useCallback(() => {
    setShowRootMenu(false);
    setShowCodeGenerator(true);
  }, [setShowRootMenu, setShowCodeGenerator]);

  // calculate widget position
  const { right, top } = useMemo(() => {
    const rect = activeCell.node.getBoundingClientRect();
    return {
      right: window.innerWidth - rect.width - rect.left + 187,
      top: rect.top + 36
    };
  }, [activeCell]);

  return (
    <div id="copilot_menu_root">
      {showRootMenu && (
        <div
          style={{
            position: 'absolute',
            right,
            top,
            display: 'block'
          }}
        >
          <Menu>
            <Menu.Header>Cognite AI</Menu.Header>
            <Menu.Item
              icon="Code"
              iconPlacement="left"
              onClick={onGenerateCodeClick} // TODO: figure out why tf onMouseUp doesn't work
            >
              Generate code
            </Menu.Item>
            <Menu.Item icon="Edit" iconPlacement="left" disabled>
              Edit code
            </Menu.Item>
            <Menu.Item icon="LightBulb" iconPlacement="left" disabled>
              Explain code
            </Menu.Item>
            <Menu.Item icon="Bug" iconPlacement="left" disabled>
              Fix code errors
            </Menu.Item>
          </Menu>
        </div>
      )}
      {showCodeGenerator && (
        <div
          style={{
            position: 'absolute',
            right,
            top,
            display: 'block'
          }}
        >
          <CodeGeneratorInputPanel
            sdk={sdk}
            activeCell={activeCell}
            onClose={() => setShowCodeGenerator(false)}
          />
        </div>
      )}
    </div>
  );
};

import React, { useState } from "react";
import Websocket from "react-websocket";

/**
 * WebSocketClient
 * @param {*} props
 *
 * example websocket client.
 */
const WebSocketClient = (props) => {
  const [state, setState] = useState({
    message: "I collect web socket messages.\n\n",
  });
  const handleMessage = (data) => {
    let arr;
    try {
      arr = JSON.parse(data);
    } catch {
      arr = "!!! an error occured parsing the incoming data !!!";
    }
    const message = state.message + "\n" + arr.join("\n");
    setState({ message });
  };
  return (
    <>
      ws: <pre>{state.message}</pre>
      <Websocket url="ws://localhost:4000/" onMessage={handleMessage} />
    </>
  );
};

export default WebSocketClient;

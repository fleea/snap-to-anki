"use client";

const SSEFetcher = () => {
  const obtainAPIResponse = async (apiRoute: string, apiData: any) => {
    // Initiate the first call to connect to SSE API
    const apiResponse = await fetch(apiRoute, {
      method: "POST",
      headers: {
        "Content-Type": "text/event-stream",
      },
      body: JSON.stringify(apiData),
    });

    if (!apiResponse.body) return;

    // To decode incoming data as a string
    const reader = apiResponse.body
      .pipeThrough(new TextDecoderStream())
      .getReader();

    while (true) {
      const { value, done } = await reader.read();
      if (done) {
        break;
      }
      if (value) {
        // Do something
      }
    }
  };

  return <></>;
};

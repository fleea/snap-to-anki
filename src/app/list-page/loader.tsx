import React, { useEffect, useState } from "react";

interface ContentItem {
  path: string;
  is_directory: boolean;
  event_type?: string;
}

const FolderWatcher: React.FC = () => {
  const [content, setContent] = useState<ContentItem[]>([]);

  useEffect(() => {
    const eventSource = new EventSource("http://localhost:8000/content");

    eventSource.onopen = (event) => {
      console.log("Connection opened");
    };

    eventSource.onerror = (event) => {
      console.error("EventSource failed:", event);
    };

    eventSource.onmessage = (event: MessageEvent) => {
      const data: ContentItem[] = JSON.parse(event.data);
      console.log(data);
      setContent((prevContent) => [...prevContent, ...data]);
    };

    return () => {
      eventSource.close();
    };
  }, []);

  return (
    <div>
      <h1>Folder Content</h1>
      <ul>
        {content.map((item, index) => (
          <li key={index}>
            {item.path} - {item.is_directory ? "Directory" : "File"}
            {item.event_type && ` - ${item.event_type}`}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FolderWatcher;

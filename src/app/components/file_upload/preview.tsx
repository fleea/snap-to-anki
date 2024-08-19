"use client";

import { ImageFile } from "@/app/components/file_upload/type";

interface PreviewProps {
  files: ImageFile[];
}

const Preview = ({ files }: PreviewProps) => {
  return (
    <div className="flex flex-wrap gap-2 pb-2 pt-2">
      {files.map((file) => (
        <div
          key={file.name}
          className="relative h-24 w-24 overflow-hidden rounded-lg bg-gray-800"
        >
          <img
            src={file.preview}
            alt={file.name}
            className="h-full w-full object-cover"
          />
          <div className="absolute inset-0 flex items-center justify-center bg-black bg-opacity-40">
            <div className="text-xs font-medium text-white">{file.name}</div>
          </div>
        </div>
      ))}
    </div>
  );
};
export default Preview;

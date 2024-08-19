"use client";
import Image from "@/app/components/icons/image";
import { DropzoneState } from "react-dropzone";

interface DropzoneUploadProps {
  state: DropzoneState;
}

const Upload = ({ state }: DropzoneUploadProps) => {
  const { open, getRootProps, getInputProps, isDragActive } = state;
  return (
    <div
      {...getRootProps({
        className: `dropzone m-auto flex w-full pb-2 pt-4 ${
          isDragActive && "bg-zinc-100 bg-opacity-10"
        }`,
      })}
    >
      <input {...getInputProps()} name="files" />
      <div className="flex h-full w-full flex-col items-center justify-center gap-1 text-sm leading-relaxed">
        <div className="p-2">
          <Image />
        </div>
        <div className="font-medium text-white">
          Drop your file here or
          <span className="group relative w-max">
            <span
              className="relative z-10 cursor-pointer px-1 group-hover:text-white"
              onClick={open}
            >
              browse
            </span>
            <span className="absolute bottom-0 left-0 z-0 h-0.5 w-full bg-indigo-600 transition-all group-hover:h-full"></span>
          </span>
        </div>
        <div className="text-xs">JPG, JPEG, PNG. Max 20MB each</div>
      </div>
    </div>
  );
};

export default Upload;

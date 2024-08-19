"use client";
import Select from "@/app/components/select";
import { defaultItems } from "@/app/components/select/type";
import ArrowRight from "@/app/components/icons/arrow-right";
import Upload from "@/app/components/file_upload/upload";
import { useDropzone } from "react-dropzone";
import { FormEvent, useState } from "react";
import { ImageFile } from "@/app/components/file_upload/type";
import Preview from "@/app/components/file_upload/preview";

const FileUpload = () => {
  const [files, setFiles] = useState<ImageFile[]>([]);
  const handleDrop = (acceptedFiles: File[]) => {
    const additionalFiles: ImageFile[] = acceptedFiles
      .filter(
        (file) =>
          !files.some((f) => f.name === file.name && f.size === file.size),
      )
      .map((file) =>
        Object.assign(file, {
          preview: URL.createObjectURL(file),
        }),
      );
    const newFiles = [...files, ...additionalFiles];
    setFiles(newFiles);
  };
  const state = useDropzone({
    noClick: true,
    noKeyboard: true,
    onDrop: handleDrop,
    accept: {
      "image/png": [".png", ".jpeg", ".jpg"],
      "application/pdf": [".pdf"],
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        [".docx"],
      "application/msword": [".doc"],
      "text/plain": [".txt"],
    },
  });

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const form = e.currentTarget;
    const formData = new FormData(form);
    files.forEach((file) => {
      formData.append("files", file);
    });
    try {
      const response = await fetch("/api/up", {
        method: "POST",
        body: formData,
      });
      const result = await response.json();
      console.log(result);
      // Handle the response as needed
    } catch (error) {
      console.error("Error uploading files:", error);
    }
  };

  return (
    <div className="flex w-full flex-col gap-6 rounded-xl bg-gray-900 p-3 text-zinc-400 shadow-lg shadow-black/40 sm:max-w-xl">
      <form onSubmit={handleSubmit}>
        <div>
          <Upload state={state} />
          <Preview files={files} />
        </div>
        <div className="flex w-full justify-between gap-2">
          <div className="flex flex-1 gap-1 sm:gap-2">
            <Select items={defaultItems} />
          </div>
          <div className="cursor-not-allowed" data-state="closed">
            <button
              className="focus-visible:ring-ring flex h-8 w-8 shrink-0 items-center justify-center whitespace-nowrap rounded-md bg-transparent text-sm font-medium text-white transition-colors hover:bg-gray-800 focus-visible:bg-gray-800 focus-visible:outline-none focus-visible:ring-0 disabled:pointer-events-none disabled:opacity-50"
              id="send-button"
              type="submit"
            >
              <ArrowRight />
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};

export default FileUpload;

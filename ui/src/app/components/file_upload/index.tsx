import Select from "@/app/components/select";
import { defaultItems } from "@/app/components/select/type";
import ArrowRight from "@/app/components/icons/arrow-right";
import Image from "@/app/components/icons/image";

const uploadParameters = {
  url: "/upload",
  acceptedFiles: "image/*",
  autoHideTrigger: false,
  extensions: {},
};

const FileUpload = () => {
  return (
    <div className="flex w-full flex-col gap-6 rounded-xl bg-gray-900 p-3 text-zinc-400 shadow-lg shadow-black/40 sm:max-w-xl">
      <div data-hs-file-upload={JSON.stringify(uploadParameters)}>
        <div className="m-auto flex w-full pb-2 pt-4">
          <div className="flex h-full w-full flex-col items-center justify-center gap-1 text-sm leading-relaxed">
            <div className="p-2">
              <Image />
            </div>
            <div className="font-medium text-white">
              Drop your file here or
              <span className="group relative w-max">
                <span
                  className="relative z-10 cursor-pointer px-1 group-hover:text-white"
                  data-hs-file-upload-trigger=""
                >
                  browse
                </span>
                <span className="absolute bottom-0 left-0 z-0 h-0.5 w-full bg-indigo-600 transition-all group-hover:h-full"></span>
              </span>
            </div>
            <div className="text-xs">JPG, JPEG, PNG. Max 20MB each</div>
          </div>
        </div>
        <template data-hs-file-upload-preview=""></template>
        <div data-hs-file-upload-previews=""></div>
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
    </div>
  );
};

export default FileUpload;

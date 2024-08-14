import ListPage from "@/app/_list-page";
import FileUpload from "@/app/components/file_upload";

export default function Home() {
  return (
    <main className="min-h-screen">
      <div className="relative mb-4 flex items-center justify-center py-[26vh] pt-[18vh] text-gray-900 sm:pt-[26vh]">
        <div className="relative flex w-full flex-col items-center gap-6 px-6 text-center">
          <div className="flex w-full flex-col items-center gap-1.5">
            <h2 className="text-4xl font-semibold tracking-tighter sm:text-5xl [@media(max-width:480px)]:text-[2rem]">
              Snap to Anki
            </h2>
            <p>Generate flashcard questions from pictures</p>
          </div>
          <FileUpload />
        </div>
      </div>
      <ListPage />
    </main>
  );
}

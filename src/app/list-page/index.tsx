"use client";

import Tree from "@/app/components/tree";
import { defaultData } from "@/app/components/tree/type";
import Table from "@/app/list-page/table";
import Loader from "@/app/list-page/loader";

const ListPage = () => {
  return (
    <>
      <h2 className="p-3 text-4xl font-semibold tracking-tighter sm:text-5xl [@media(max-width:480px)]:text-[2rem]">
        View your flashcards
      </h2>
      <div className="grid grid-cols-12 gap-4 p-3">
        <div className="col-span-4">
          <Tree data={defaultData} />
        </div>
        <div className="col-span-8">
          <Loader />
          <Table />
        </div>
      </div>
    </>
  );
};

export default ListPage;

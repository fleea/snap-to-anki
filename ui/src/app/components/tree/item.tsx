import { TreeData, TreeViewProps } from "@/app/components/tree/type";
import Folder from "@/app/components/icons/folder";
import Plus from "@/app/components/icons/plus";
import File from "@/app/components/icons/file";
import Title from "@/app/components/tree/title";

interface TreeItemProps extends Omit<TreeViewProps, "data"> {
  data: TreeData;
}

const TreeItem = ({ data }: TreeItemProps) => {
  const { id, name, children } = data;
  return (
    <div
      className="hs-accordion active"
      role="treeitem"
      aria-expanded="true"
      id={`hs-basic-tree-heading-${id}`}
    >
      <div className="hs-accordion-heading flex w-full items-center gap-x-0.5 py-0.5">
        {children && (
          <button
            className="hs-accordion-toggle flex size-6 items-center justify-center rounded-md hover:bg-gray-100 focus:bg-gray-100 focus:outline-none disabled:pointer-events-none disabled:opacity-50 dark:hover:bg-neutral-700 dark:focus:bg-neutral-700"
            aria-expanded="true"
            aria-controls="hs-basic-tree-collapse-one"
          >
            <Plus />
          </button>
        )}
        <div className="hs-accordion-selectable grow cursor-pointer rounded-md px-1.5 hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700">
          <div className="flex items-center gap-x-3">
            {children && <Folder />}
            {!children && <File />}
            <div className="grow">
              <Title name={name} id={id} />
            </div>
          </div>
        </div>
      </div>
      {children && (
        <div
          id={`hs-basic-tree-collapse-${id}`}
          className="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
          role="group"
          aria-labelledby="hs-basic-tree-heading-one"
        >
          <div
            className="hs-accordion-group relative ps-7 before:absolute before:start-3 before:top-0 before:-ms-px before:h-full before:w-0.5 before:bg-gray-100 dark:before:bg-neutral-700"
            role="group"
            data-hs-accordion-always-open=""
          >
            {children.map((child) => (
              <TreeItem key={child.id} data={child} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default TreeItem;

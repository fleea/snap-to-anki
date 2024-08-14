"use client";

import { defaultItems, DropdownItem } from "@/app/components/dropdown/type";
import DropdownItemComponent from "@/app/components/dropdown/item";
import Caret from "@/app/components/icons/caret";

interface DropdownProps {
  items: DropdownItem[];
  active?: string;
}

const Dropdown = ({
  items = defaultItems,
  active: string = "basic_reversed",
}: DropdownProps) => {
  const selectedItem = items.find((item) => item.value === string);
  return (
    <div className="hs-dropdown relative z-10 inline-flex">
      <button
        id="hs-dropdown-default"
        type="button"
        className="hs-dropdown-toggle inline-flex items-center gap-x-2 rounded-lg border border-gray-200 bg-white px-4 py-3 text-sm font-medium text-gray-800 shadow-sm hover:bg-gray-50 focus:bg-gray-50 focus:outline-none disabled:pointer-events-none disabled:opacity-50 dark:border-neutral-700 dark:bg-neutral-800 dark:text-white dark:hover:bg-neutral-700 dark:focus:bg-neutral-700"
        aria-haspopup="menu"
        aria-expanded="false"
        aria-label="Dropdown"
      >
        {selectedItem?.label || "Select"}
        <Caret />
      </button>
      <div
        className="hs-dropdown-menu duration mt-2 hidden min-w-60 space-y-0.5 rounded-lg bg-white p-1 opacity-0 shadow-md transition-[opacity,margin] before:absolute before:-top-4 before:start-0 before:h-4 before:w-full after:absolute after:-bottom-4 after:start-0 after:h-4 after:w-full hs-dropdown-open:opacity-100 dark:divide-neutral-700 dark:border dark:border-neutral-700 dark:bg-neutral-800"
        role="menu"
        aria-orientation="vertical"
        aria-labelledby="hs-dropdown-default"
      >
        {items.map((item) => (
          <DropdownItemComponent item={item} />
        ))}
      </div>
    </div>
  );
};

export default Dropdown;

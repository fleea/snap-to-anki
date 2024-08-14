"use client";

import { DropdownItem } from "@/app/components/dropdown/type";

interface DropdownItemProps {
  item: DropdownItem;
}

const DropdownItemComponent = ({ item }: DropdownItemProps) => {
  return (
    <a
      className="flex items-center gap-x-3.5 rounded-lg px-3 py-2 text-sm text-gray-800 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700"
      href="#"
    >
      {item.label}
    </a>
  );
};

export default DropdownItemComponent;

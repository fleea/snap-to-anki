import { defaultItems, SelectItem } from "@/app/components/select/type";

interface SelectProps {
  items: SelectItem[];
  value?: string;
}

const Select = ({
  items = defaultItems,
  value = "basic_reversed",
}: SelectProps) => {
  return (
    <select
      defaultValue={value}
      className="focus-visible:ring-ring block h-8 rounded-md border-r-[8px] border-r-transparent bg-gray-800 px-2 py-2 text-sm text-white/70 transition-colors focus-within:bg-gray-700 hover:bg-gray-700/70 hover:text-white focus-visible:bg-gray-800 focus-visible:outline-none focus-visible:ring-0 disabled:pointer-events-none disabled:opacity-50"
    >
      {items.map((item) => (
        <option key={item.value} value={item.value} disabled={!item.available}>
          {item.label}
        </option>
      ))}
    </select>
  );
};

export default Select;

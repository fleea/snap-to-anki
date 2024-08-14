export interface DropdownItem {
  label: string;
  value: string;
}

export const defaultItems: DropdownItem[] = [
  {
    label: "Basic",
    value: "basic",
  },
  {
    label: "Basic (and reversed card)",
    value: "basic_reversed",
  },
  {
    label: "Cloze",
    value: "cloze",
  },
  {
    label: "Image Occlusion",
    value: "image_occlusion",
  },
  {
    label: "Fill-in-the-blank",
    value: "fill_in_blank",
  },
  {
    label: "Multiple Choice",
    value: "multiple_choice",
  },
  {
    label: "True/False",
    value: "true_false",
  },
  {
    label: "Audio",
    value: "audio",
  },
  {
    label: "Basic (optional reversed card)",
    value: "basic_optional_reversed",
  },
  {
    label: "Type in the answer",
    value: "type_answer",
  },
];

export interface SelectItem {
  label: string;
  value: string;
  available: boolean;
}

export const defaultItems: SelectItem[] = [
  {
    label: "Basic",
    value: "basic",
    available: true,
  },
  {
    label: "Basic (and reversed card)",
    value: "basic_reversed",
    available: true,
  },
  {
    label: "Cloze",
    value: "cloze",
    available: false,
  },
  {
    label: "Image Occlusion",
    value: "image_occlusion",
    available: false,
  },
  {
    label: "Fill-in-the-blank",
    value: "fill_in_blank",
    available: false,
  },
  {
    label: "Multiple Choice",
    value: "multiple_choice",
    available: false,
  },
  {
    label: "True/False",
    value: "true_false",
    available: false,
  },
  {
    label: "Audio",
    value: "audio",
    available: false,
  },
  {
    label: "Basic (optional reversed card)",
    value: "basic_optional_reversed",
    available: false,
  },
  {
    label: "Type in the answer",
    value: "type_answer",
    available: false,
  },
];

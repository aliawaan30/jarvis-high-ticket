import { clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs) {
  return twMerge(clsx(inputs))
} 


// Guarded: Base44 renders pages on its server first, where there is no window.
export const isIframe = typeof window !== 'undefined' && window.self !== window.top;
